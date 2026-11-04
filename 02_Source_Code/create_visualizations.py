"""
Create the project's static plots from the cleaned CSV using pandas/matplotlib.
This script is independent of Hive and is useful if the metastore is unavailable.

Run:
    python 02_Source_Code/create_visualizations.py \
        --input 01_Dataset/traffic_cleaned.csv --output 04_Results
"""
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="01_Dataset/traffic_cleaned.csv")
    parser.add_argument("--output", default="04_Results")
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)
    if "congestion" in df.columns:
        df = df[df["congestion"].astype(str).str.lower() != "congestion"].copy()
    df["traffic_volume"] = pd.to_numeric(df["traffic_volume"], errors="coerce")
    df["hour"] = pd.to_numeric(df["hour"], errors="coerce")
    df = df.dropna(subset=["traffic_volume"])

    if "congestion" in df.columns:
        counts = df.groupby("congestion").size().sort_index()
        ax = counts.plot(kind="bar", figsize=(7, 5))
        ax.set_title("Traffic Congestion Distribution")
        ax.set_ylabel("Number of Records")
        plt.tight_layout()
        plt.savefig(out / "congestion_distribution.png", dpi=300)
        plt.close()

    if "hour" in df.columns:
        hourly = df.groupby("hour")["traffic_volume"].mean().sort_index()
        ax = hourly.plot(kind="line", marker="o", figsize=(8, 5))
        ax.set_title("Average Traffic Volume by Hour")
        ax.set_xlabel("Hour of Day")
        ax.set_ylabel("Average Traffic Volume")
        plt.tight_layout()
        plt.savefig(out / "traffic_by_hour.png", dpi=300)
        plt.close()

    if "weather_main" in df.columns:
        weather = df.groupby("weather_main")["traffic_volume"].mean().sort_values(ascending=False)
        ax = weather.plot(kind="bar", figsize=(10, 5))
        ax.set_title("Weather Impact on Traffic Volume")
        ax.set_ylabel("Average Traffic Volume")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(out / "weather_impact.png", dpi=300)
        plt.close()

    print(f"Charts saved to: {out.resolve()}")

if __name__ == "__main__":
    main()
