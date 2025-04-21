import os
import shutil
from datetime import datetime

def log_to_dashboard(csv_filepath):
    """
    Copies the summary CSV file to the dashboard_logs directory with a timestamped filename.
    """
    dashboard_dir = "dashboard_logs"
    os.makedirs(dashboard_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_filename = f"anomaly_summary_{timestamp}.csv"
    dest_path = os.path.join(dashboard_dir, dest_filename)

    # Copy file
    shutil.copy(csv_filepath, dest_path)
    print(f"🖥️  Summary CSV logged to dashboard at: {dest_path}")
