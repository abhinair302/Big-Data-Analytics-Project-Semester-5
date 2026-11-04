# TrafficSense — Presentation Notes

## 1. Project Overview
TrafficSense is a Big Data Analytics project that studies historical traffic volume, congestion patterns, and weather-related traffic trends using the Metro Interstate Traffic Volume dataset.

## 2. Problem Statement
Traffic patterns vary by time and weather. Analyzing historical data helps identify peak traffic periods, understand congestion distribution, and explore machine-learning-based traffic prediction.

## 3. Objectives
- Analyze historical traffic volume and congestion.
- Study hourly and weather-related patterns.
- Process and query data using Hadoop, HDFS, Hive, and Spark.
- Experiment with Random Forest classification and next-hour traffic prediction.
- Present findings through visualizations and Power BI.

## 4. Technology Stack
- Hadoop and HDFS: distributed storage infrastructure.
- Hive: SQL-like querying and analytical summaries.
- Spark/PySpark: data processing and machine learning.
- Random Forest: classification model.
- Python and Matplotlib: visualizations.
- Power BI: interactive dashboard.

## 5. Dataset
Dataset: Metro Interstate Traffic Volume.
Valid records used in the analysis: 48,187 after removing an accidental header row.
Important attributes include traffic volume, date and time, temperature, rainfall, snowfall, cloud coverage, and weather information.

## 6. Project Workflow
1. Load and clean the traffic dataset.
2. Store and query data through the Hadoop/Hive environment.
3. Use Spark to perform traffic and weather analysis.
4. Generate charts and model evaluation results.
5. Present the results in the existing Power BI dashboard.

## 7. Analytical Findings
- Congestion categories in the cleaned analysis:
  - High: 11,353 records
  - Medium: 21,618 records
  - Low: 15,216 records
- Average traffic volume is highest around the afternoon and evening peak periods in the recorded hourly analysis.
- Weather categories show differences in average observed traffic volume.
These are descriptive findings from the historical dataset and do not establish that weather alone causes congestion.

## 8. Machine Learning
A next-hour prediction experiment used hourly aggregates, retained consecutive observations exactly one hour apart, and used a chronological train/test split.

- Training examples: 30,388
- Test examples: 7,598
- Random Forest: 50 trees, maximum depth 10
- Historical test accuracy: 93.18%

This is historical evaluation performance, not a guarantee of real-world performance. Verify the model's class-label mapping before interpreting an individual prediction.

An earlier classifier reported 98.30% accuracy while using traffic volume to predict a congestion label derived from traffic volume. This introduces target leakage, so it should not be presented as independent forecasting accuracy.

## 9. Dashboard Demonstration
Open `05_Dashboard/hello.pbix` in Power BI Desktop.

Suggested order:
1. Introduce the dashboard title and project purpose.
2. Explain the KPI cards.
3. Show congestion distribution.
4. Explain hourly traffic trends.
5. Discuss weather-related traffic patterns.
6. Explain the predicted congestion distribution, clarifying that it is a model output.

## 10. Limitations
- The data is historical.
- Model performance on a historical test set does not guarantee live prediction performance.
- The earlier 98.30% result is affected by target leakage.
- Individual next-hour predictions should not be assigned a congestion name until the label mapping is verified.
- Confirm Hadoop, Hive, and HDFS availability before a live terminal demonstration.

## 11. Project Artifacts
- `01_Dataset/`: original and cleaned CSV files
- `02_Source_Code/`: notebook and Python scripts
- `03_Hive_SQL/`: Hive analysis queries
- `04_Results/`: charts and CSV results
- `05_Dashboard/hello.pbix`: Power BI dashboard
- `06_Documentation/`: project notes and checklist

## 12. Closing Statement
TrafficSense demonstrates a workflow combining big-data storage and analysis, machine-learning experimentation, and business intelligence visualization to explore urban traffic patterns.
