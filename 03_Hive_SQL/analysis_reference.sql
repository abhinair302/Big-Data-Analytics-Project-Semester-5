-- TrafficSense Hive analysis queries.
-- These query patterns are based on the saved Hive Results.docx.
-- Execute only after the Hive metastore and traffic_db.traffic_data are available.
USE traffic_db;

DESCRIBE traffic_data;

-- Overall congestion distribution
SELECT congestion, COUNT(*) AS record_count
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY congestion
ORDER BY congestion;

-- Average traffic volume by congestion category
SELECT congestion, AVG(traffic_volume) AS average_traffic_volume
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY congestion;

-- Peak hours
SELECT hour, AVG(traffic_volume) AS avg_volume
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY hour
ORDER BY avg_volume DESC;

-- Weather versus average traffic volume
SELECT weather_main, AVG(traffic_volume) AS avg_volume
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY weather_main
ORDER BY avg_volume DESC;

-- Day-of-week traffic pattern
SELECT day_of_week, AVG(traffic_volume) AS avg_volume
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY day_of_week
ORDER BY day_of_week;

-- Monthly traffic trend
SELECT month, AVG(traffic_volume) AS avg_volume
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY month
ORDER BY month;

-- High congestion examples
SELECT date_time, traffic_volume, weather_main
FROM traffic_data
WHERE congestion = 'High'
LIMIT 20;

-- Hour-by-congestion counts
SELECT hour, congestion, COUNT(*) AS record_count
FROM traffic_data
WHERE congestion <> 'congestion'
GROUP BY hour, congestion
ORDER BY hour, congestion;
