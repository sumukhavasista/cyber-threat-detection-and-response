import pandas as pd
import joblib
import os
from response.response import trigger_response

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "final_cleaned_system_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "isolation_forest_model.pkl")
ANOMALY_LOG_PATH = os.path.join(BASE_DIR, "logs", "anomalies.log")

# Load the dataset
data = pd.read_csv(DATA_PATH)

# Drop timestamp column if it exists (should match training setup)
if 'timestamp' in data.columns:
    data = data.drop(columns=['timestamp'])

# Load the trained Isolation Forest model
model = joblib.load(MODEL_PATH)

# Predict anomalies
data["anomaly"] = model.predict(data)

# Extract only anomalies
anomalies_df = data[data["anomaly"] == -1]

# Log anomalies to a separate log file
if not anomalies_df.empty:
    os.makedirs(os.path.dirname(ANOMALY_LOG_PATH), exist_ok=True)
    anomalies_df.to_csv(ANOMALY_LOG_PATH, index=False)
    print(f"🚨 {len(anomalies_df)} anomalies detected and logged to 'logs/anomalies.log'")
    trigger_response(anomalies_df)
else:
    print("✅ No anomalies detected.")
