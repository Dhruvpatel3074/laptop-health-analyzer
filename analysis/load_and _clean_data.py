import pandas as pd
import os

# -------------------------------
# Path handling (robust & safe)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "system_stats.csv")

# -------------------------------
# Load the dataset
# -------------------------------
df = pd.read_csv(DATA_PATH)

print("✅ Data loaded successfully")
print("Shape:", df.shape)

# -------------------------------
# Convert timestamp to datetime
# -------------------------------
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# -------------------------------
# Handle missing values
# -------------------------------
df["Battery (%)"] = pd.to_numeric(df["Battery (%)"], errors="coerce")
df["CPU Usage (%)"] = pd.to_numeric(df["CPU Usage (%)"], errors="coerce")
df["RAM Usage (%)"] = pd.to_numeric(df["RAM Usage (%)"], errors="coerce")
df["Disk Usage (%)"] = pd.to_numeric(df["Disk Usage (%)"], errors="coerce")

# -------------------------------
# Sort data by time
# -------------------------------
df = df.sort_values("Timestamp")

# -------------------------------
# Basic data validation
# -------------------------------
print("\n📊 Data Info:")
print(df.info())

print("\n📈 First 5 rows:")
print(df.head())

print("\n📉 Last 5 rows:")
print(df.tail())
