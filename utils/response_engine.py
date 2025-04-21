import pandas as pd
import os

def respond_to_anomalies(csv_path):
    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    for index, row in df.iterrows():
        severity = row['Severity']
        timestamp = row.get('timestamp', 'Unknown time')
        details = f"Anomaly at {timestamp} - Score: {row['Anomaly Score']}"

        if severity == 'Low':
            log_action(details, severity)
        elif severity == 'Medium':
            alert_admin(details)
        elif severity == 'High':
            take_emergency_action(details)
        else:
            print(f"⚠️ Unknown severity level: {severity}")

def log_action(details, severity):
    print(f"[LOG] ({severity}) {details}")

def alert_admin(details):
    print(f"[ALERT] 🚨 Notify admin: {details}")
    # Future: send email/Slack alert

def take_emergency_action(details):
    print(f"[EMERGENCY] 🔐 Triggering response: {details}")
    # Future: add automated remediation like system shutdown, isolation, etc.
