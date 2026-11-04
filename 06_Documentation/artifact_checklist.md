# TrafficSense artifact checklist

## Present in the project folder
- [x] Original Metro Interstate Traffic Volume CSV
- [x] Cleaned CSV
- [x] Initial Jupyter notebook
- [x] Existing Power BI dashboard copy (`05_Dashboard/hello.pbix`)
- [x] Congestion distribution chart
- [x] Feature importance chart and CSV
- [x] Hourly traffic chart
- [x] Weather impact chart
- [x] Next-hour forecast evaluation CSV
- [x] Main project README

## Added as documented code references
- [x] Hive analysis SQL reference
- [x] Spark Hive analysis script
- [x] Local CSV visualization script
- [x] Next-hour model training reconstruction

## Verify before presentation
- [ ] Hive metastore starts successfully and `SHOW DATABASES;` works
- [ ] Confirm table schemas before rerunning SQL
- [ ] Locate/copy any additional original Spark source notebooks or scripts
- [ ] Verify dashboard opens and has the expected TrafficSense visuals
- [ ] Do not claim the model's next-hour label mapping is verified unless checked
- [ ] Explain 93.18% as historical chronological test accuracy
- [ ] Do not present the earlier 98.30% result as independent forecasting accuracy; it used `traffic_volume` to predict a label derived from that same field
