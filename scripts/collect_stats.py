import psutil
import csv
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def collect_system_stats():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else "N/A"
    charging = battery.power_plugged if battery else "N/A"

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    data = [
        timestamp,
        battery_percent,
        charging,
        cpu_usage,
        ram_usage,
        disk_usage
    ]

    data_dir = os.path.join(BASE_DIR, "..", "data")
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, "system_stats.csv")


    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Battery (%)",
                "Charging",
                "CPU Usage (%)",
                "RAM Usage (%)",
                "Disk Usage (%)"
            ])

        writer.writerow(data)

    print("✅ System stats recorded successfully!")
    print(f"Battery: {battery_percent}% | CPU: {cpu_usage}% | RAM: {ram_usage}%")

if __name__ == "__main__":
    collect_system_stats()
