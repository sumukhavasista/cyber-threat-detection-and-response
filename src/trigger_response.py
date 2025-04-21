# src/trigger_response.py

import pandas as pd
from pathlib import Path

# Load categorized anomalies
output_path = Path("..") / "data" / "output" / "categorized_anomalies.csv"
df = pd.read_csv(output_path)

# Simulate different responses based on severity
print("⚠️ Triggering response for anomalies...")

for _, row in df.iterrows():
    severity = row['severity']
    score = row['anomaly_score']

    if severity == 'Low':
        print(f"[LOW] Anomaly with score {score:.4f} logged.")
    
    elif severity == 'Medium':
        print(f"[MEDIUM] ⚠️ Warning! Anomaly detected with score {score:.4f}")
    
    elif severity == 'High':
        print(f"[HIGH] 🚨 CRITICAL ALERT! Severe anomaly detected with score {score:.4f}")
        # You can simulate a real-world action here like sending an email or notification
        # e.g., send_alert(score)

print("✅ Response handling complete.")
