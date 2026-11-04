"""
TrafficSense - next-hour congestion prediction experiment (PySpark MLlib).

This is a clean, documented reconstruction based on the recorded experiment:
hourly observations, consecutive-hour filtering, chronological train/test split,
Random Forest with 50 trees, maxDepth=10, seed=42.

Run from the project root in an environment with Spark/Hive access:
    spark-submit 02_Source_Code/train_next_hour_model.py

It trains a fresh pipeline model and saves to a NEW local path by default.
It does not overwrite the existing HDFS model.
"""
import argparse
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import (
    avg, col, first, lead, hour, month, dayofweek, row_number, to_timestamp
)
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

FEATURES = [
    "traffic_volume", "temp", "rain_1h", "snow_1h", "clouds_all",
    "hour", "day_of_week", "month", "weather_index"
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="/home/abhijeet/TrafficSense_Project/02_Source_Code/next_hour_model_pipeline"
    )
    parser.add_argument("--test-fraction", type=float, default=0.2)
    args = parser.parse_args()
    if not 0.05 <= args.test_fraction <= 0.5:
        raise ValueError("--test-fraction must be between 0.05 and 0.5")

    spark = (
        SparkSession.builder.appName("TrafficSense-NextHour-RandomForest")
        .enableHiveSupport().getOrCreate()
    )
    try:
        raw = spark.table("traffic_db.traffic_data")
        raw = raw.filter(col("congestion") != "congestion")
        raw = raw.withColumn("date_time", to_timestamp("date_time"))

        # The dataset is hourly. Aggregate defensively if duplicate timestamps exist.
        hourly = raw.groupBy("date_time").agg(
            avg("traffic_volume").alias("traffic_volume"),
            avg("temp").alias("temp"),
            avg("rain_1h").alias("rain_1h"),
            avg("snow_1h").alias("snow_1h"),
            avg("clouds_all").alias("clouds_all"),
            first("weather_main", ignorenulls=True).alias("weather_main"),
            first("congestion", ignorenulls=True).alias("congestion"),
        )

        hourly = (
            hourly.withColumn("hour", hour("date_time"))
            .withColumn("day_of_week", dayofweek("date_time"))
            .withColumn("month", month("date_time"))
        )

        # Label is congestion at the next observation; keep only exact 1-hour gaps.
        w = Window.orderBy("date_time")
        temporal = (
            hourly
            .withColumn("next_time", lead("date_time").over(w))
            .withColumn("next_congestion", lead("congestion").over(w))
            .withColumn(
                "gap_seconds",
                col("next_time").cast("long") - col("date_time").cast("long")
            )
            .filter(col("gap_seconds") == 3600)
            .dropna(subset=FEATURES + ["next_congestion"])
        )

        w2 = Window.orderBy("date_time")
        temporal = temporal.withColumn("_row_number", row_number().over(w2))
        total = temporal.count()
        split_at = int(total * (1.0 - args.test_fraction))
        if total < 10 or split_at <= 0 or split_at >= total:
            raise ValueError(f"Not enough consecutive hourly examples for split: {total}")

        train = temporal.filter(col("_row_number") <= split_at).drop("_row_number")
        test = temporal.filter(col("_row_number") > split_at).drop("_row_number")

        weather_indexer = StringIndexer(
            inputCol="weather_main", outputCol="weather_index",
            handleInvalid="keep"
        )
        label_indexer = StringIndexer(
            inputCol="next_congestion", outputCol="label",
            handleInvalid="skip"
        )
        assembler = VectorAssembler(inputCols=FEATURES, outputCol="features")
        rf = RandomForestClassifier(
            featuresCol="features", labelCol="label",
            numTrees=50, maxDepth=10, seed=42
        )
        pipeline = Pipeline(stages=[weather_indexer, label_indexer, assembler, rf])
        model = pipeline.fit(train)
        predictions = model.transform(test)
        accuracy = MulticlassClassificationEvaluator(
            labelCol="label", predictionCol="prediction", metricName="accuracy"
        ).evaluate(predictions)

        print(f"Consecutive-hour examples: {total}")
        print(f"Training examples: {split_at}")
        print(f"Test examples: {total - split_at}")
        print(f"Chronological test accuracy: {accuracy:.4%}")
        predictions.select(
            "date_time", "next_time", "next_congestion", "prediction", "probability"
        ).show(10, truncate=False)
        model.write().overwrite().save(args.output)
        print(f"Pipeline model saved to: {args.output}")
        print("Note: this is historical test performance, not a guarantee of live accuracy.")
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
