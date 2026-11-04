# TrafficSense: Urban Traffic Flow Analytics & Congestion Prediction

## 1. Project Overview
TrafficSense is a traffic analytics and congestion prediction project using the Metro Interstate Traffic Volume dataset. It combines big data technologies, machine learning, and business intelligence to analyze traffic patterns and present insights through a Power BI dashboard.

## 2. Objectives
- Analyze historical traffic volume and congestion patterns.
- Study traffic variation by hour, weather, and other available features.
- Use Apache Hadoop and Hive for big data storage and analysis.
- Use Apache Spark MLlib and Random Forest for traffic classification and next-hour prediction experiments.
- Present analytical results using Power BI visualizations.

## 3. Technologies
- Apache Hadoop / HDFS
- Apache Hive
- Apache Spark / PySpark
- Python and Jupyter Notebook
- Random Forest classification
- Microsoft Power BI

## 4. Dataset
- Original dataset: `01_Dataset/Metro_Interstate_Traffic_Volume.csv`
- Cleaned dataset: `01_Dataset/traffic_cleaned.csv`
- Initial notebook: `02_Source_Code/first_stage.ipynb`

The project analysis used 48,187 valid records after removing an accidental header row. The dataset contains traffic volume, time-related fields, weather information, and related attributes.

## 5. Model Results
A next-hour traffic forecasting experiment used hourly aggregates and a chronological train/test split. Only consecutive hourly observations were retained.

- Training examples: 30,388
- Test examples: 7,598
- Random Forest: 50 trees, maximum depth 10
- Historical test accuracy: 93.18%

This accuracy is from a historical test set and should not be interpreted as live or future real-world performance.

An earlier classifier achieved 98.30% accuracy using traffic volume to derive the congestion label. Because traffic volume directly determines that label, this result is affected by target leakage and should not be presented as an independent forecasting result.

## 6. Dashboard
The existing Power BI report contains:
- KPI cards for average traffic and record count
- Congestion distribution
- Hourly traffic trends
- Weather-related traffic analysis
- Predicted congestion distribution

Copy the original `.pbix` report into `05_Dashboard/` when its exact location is confirmed. Keep the original dashboard unchanged.

## 7. Project Folder Structure
- `01_Dataset/` — original and cleaned CSV datasets
- `02_Source_Code/` — Jupyter notebook and source scripts
- `03_Hive_SQL/` — Hive SQL scripts
- `04_Results/` — evaluation CSV files and visualization images
- `05_Dashboard/` — Power BI report
- `06_Documentation/` — project report, presentation notes, and supporting documentation

## 8. Current Artifact Status
The original dataset, cleaned dataset, initial notebook, and six result files have been copied into this project folder.

The saved Spark Random Forest models are currently stored in HDFS:
- `/user/abhijeet/traffic_rf_model`
- `/user/abhijeet/traffic_next_hour_rf_model`

Hive previously contained traffic-analysis tables, but the current Hive command returned a metastore-client error. Verify Hive connectivity before demonstrating Hive live. The HDFS services were successfully started during project preparation.

The original Power BI report and additional source scripts still need to be located and copied into this folder.

## 9. Limitations
- Results are based on historical data.
- Model accuracy does not guarantee real-world prediction performance.
- The earlier 98.30% classifier result is affected by target leakage.
- The next-hour model's historical test accuracy is 93.18%; class-label mapping and inference should be verified before demonstrating a specific live prediction.

## 10. Reproducibility
Use the saved notebook, datasets, model artifacts, SQL scripts, and evaluation results to document and reproduce the workflow. Do not claim that an artifact is available or executable unless it has been verified.

## 11. Author
TrafficSense — Big Data Analytics Project
