"""
TrafficSense - Spark analysis against the Hive traffic_db.traffic_data table.

Run from an environment where PySpark can connect to the Hive metastore:
    spark-submit 02_Source_Code/spark_hive_analysis.py

This script reflects analysis operations shown in the project Word notes.
It filters the accidental CSV header row that was imported as a record.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, to_timestamp

spark = (
    SparkSession.builder
    .appName("TrafficSense-Hive-Analysis")
    .enableHiveSupport()
    .getOrCreate()
)

SOURCE = "traffic_db.traffic_data"

try:
    df = spark.table(SOURCE)
    # The imported CSV header accidentally appears as a data row.
    df = df.filter(col("congestion") != "congestion")
    df = df.withColumn("date_time", to_timestamp("date_time"))

    print("Valid row count:", df.count())
    df.groupBy("congestion").agg(count("*").alias("records")).orderBy("congestion").show()
    df.groupBy("congestion").agg(avg("traffic_volume").alias("avg_traffic")).orderBy("congestion").show()
    df.groupBy("hour").agg(avg("traffic_volume").alias("average_traffic_volume")).orderBy(col("average_traffic_volume").desc()).show(24, truncate=False)
    df.groupBy("weather_main").agg(avg("traffic_volume").alias("average_traffic_volume")).orderBy(col("average_traffic_volume").desc()).show(truncate=False)
    df.groupBy("day_of_week").agg(avg("traffic_volume").alias("average_traffic_volume")).orderBy("day_of_week").show()
    df.groupBy("month").agg(avg("traffic_volume").alias("average_traffic_volume")).orderBy("month").show()
    df.filter(col("congestion") == "High").select("date_time", "traffic_volume", "weather_main").show(20, truncate=False)

    # Write summary tables. These overwrite only the named derived Hive tables.
    df.groupBy("congestion").agg(count("*").alias("record_count")) \
        .write.mode("overwrite").saveAsTable("traffic_db.congestion_summary")
    df.groupBy("hour").agg(avg("traffic_volume").alias("average_traffic_volume")) \
        .write.mode("overwrite").saveAsTable("traffic_db.hourly_traffic")
    df.groupBy("weather_main").agg(avg("traffic_volume").alias("average_traffic_volume")) \
        .write.mode("overwrite").saveAsTable("traffic_db.weather_analysis")
finally:
    spark.stop()
