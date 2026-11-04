# TrafficSense: Urban Traffic Flow Analytics & Congestion Prediction

## 1. Project Overview
TrafficSense analyzes historical urban traffic volume and congestion patterns using big data technologies, machine learning, and business intelligence. The project uses the Metro Interstate Traffic Volume dataset and presents insights through a Power BI dashboard.

## 2. Objectives
- Analyze traffic volume and congestion distribution.
- Examine traffic patterns by hour, weather, and time-related attributes.
- Use Hadoop/HDFS and Hive for data storage and analytical queries.
- Use Spark MLlib and Random Forest for congestion classification and next-hour prediction experiments.
- Communicate findings through charts and a Power BI dashboard.

## 3. Technology Stack
- Apache Hadoop and HDFS
- Apache Hive
- Apache Spark / PySpark and MLlib
- Python, pandas, and Matplotlib
- Random Forest classification
- Microsoft Power BI
- Jupyter Notebook

## 4. Dataset
- Original CSV: `01_Dataset/Metro_Interstate_Traffic_Volume.csv`
- Cleaned CSV: `01_Dataset/traffic_cleaned.csv`
- Initial notebook: `02_Source_Code/first_stage.ipynb`

The analysis contains 48,187 valid records after removing an accidental header row. The data includes traffic volume, timestamps, weather conditions, and related attributes.

## 5. Machine Learning Results
The next-hour prediction experiment uses hourly aggregates and retains consecutive observations exactly one hour apart.

- Training examples: 30,388
- Test examples: 7,598
- Model: Random Forest, 50 trees, maximum depth 10
- Chronological historical test accuracy: 93.18%

This is a historical test result, not a guarantee of live forecasting performance. Verify model execution and class-label mapping before demonstrating a specific prediction.

An earlier classifier reported 98.30% accuracy while using traffic volume to predict a congestion label derived from traffic volume. This introduces target leakage, so that result should not be presented as independent forecasting performance.

## 6. Hive Analysis
The Hive analysis reference includes queries for:
- Congestion distribution and average traffic by congestion level
- Traffic volume by hour and day of the week
- Monthly traffic trends
- Weather-related traffic patterns
- High-congestion records

The reference SQL is in `03_Hive_SQL/analysis_reference.sql`. Confirm Hive connectivity before a live demonstration.

## 7. Power BI Dashboard
Dashboard file: `05_Dashboard/hello.pbix`

The existing report includes KPI cards, congestion distribution, hourly traffic trends, weather analysis, and predicted congestion distribution. Preserve the existing report and use it for the presentation.

## 8. Project Structure
- `01_Dataset/` — original and cleaned datasets
- `02_Source_Code/` — notebook, Spark analysis, model-training, and visualization scripts
- `03_Hive_SQL/` — Hive analysis queries
- `04_Results/` — charts and CSV results
- `05_Dashboard/` — Power BI report
- `06_Documentation/` — artifact checklist and supporting project notes

## 9. Important Limitations
- The analysis uses historical data.
- Historical accuracy does not establish real-world or live prediction accuracy.
- The earlier 98.30% result is affected by target leakage.
- The next-hour prediction's class-label mapping should be verified before interpreting individual predicted classes.
- The saved Spark models are expected in HDFS at `/user/abhijeet/traffic_rf_model` and `/user/abhijeet/traffic_next_hour_rf_model`; verify availability before relying on them in a live demo.

## 10. Source Files
- `02_Source_Code/spark_hive_analysis.py` — Spark/Hive analysis workflow
- `02_Source_Code/train_next_hour_model.py` — reconstructed next-hour model-training workflow; test before claiming exact reproducibility
- `02_Source_Code/create_visualizations.py` — chart-generation script
- `03_Hive_SQL/analysis_reference.sql` — Hive analysis queries

## 11. Reproducibility
Check the README files in `02_Source_Code/` and `03_Hive_SQL/` before running scripts. Confirm dependencies, input paths, Hive availability, and HDFS model paths. Do not overwrite existing dashboard or result artifacts without a backup.

## 12. Project
TrafficSense — Big Data Analytics Project
