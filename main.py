import pandas as pd
import joblib
from response import collect_anomaly, finalize_response
from severity_mapper import determine_severity

# Load model and data
model = joblib.load("models/isolation_forest_model.pkl")
df = pd.read_csv("data/processed/final_cleaned_system_data.csv")

# Predict anomalies
df["anomaly"] = model.predict(df)
anomalies = df[df["anomaly"] == -1]

# Determine severity
anomalies["severity"] = anomalies.apply(determine_severity, axis=1)

# Collect anomalies for summary response
for _, row in anomalies.iterrows():
    collect_anomaly(row)

# Trigger final response (email + dashboard + containment)
finalize_response()
