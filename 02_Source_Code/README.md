# Source code

- `first_stage.ipynb` — original initial notebook copied from the project folder.
- `spark_hive_analysis.py` — Spark queries and derived Hive summary tables based on the saved development notes.
- `create_visualizations.py` — local CSV-to-chart script; useful if Hive is unavailable.
- `train_next_hour_model.py` — reproducible next-hour model training template based on the recorded approach (hourly records, consecutive-hour filtering, chronological split, Random Forest 50 trees / depth 10).

Important: the next-hour script is a clean reconstruction from recorded project settings, not a byte-for-byte copy of today's interactive shell commands. Test it in your Spark/Hive environment before claiming it reruns the exact saved model. It writes a fresh pipeline model to a local path and does not overwrite the existing HDFS model.
