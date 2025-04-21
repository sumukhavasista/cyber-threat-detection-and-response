
import pandas as pd
import joblib
from pathlib import Path

# Define paths
data_path = Path("../data/processed/final_cleaned_system_data.csv")
model_path = Path("../models/isolation_forest_model.pkl")
output_path = Path("../data/output/anomaly_output.csv")

# Load the data
df = pd.read_csv(data_path)

# Load the trained Isolation Forest model
model = joblib.load(model_path)

# Drop any columns that were not used during training
# Common columns to ignore: 'anomaly', 'anomaly_score'
features = df.drop(columns=['anomaly', 'anomaly_score'], errors='ignore')

# Get anomaly scores from the model
df['anomaly_score'] = model.decision_function(features)

# Predict anomaly labels (-1 for anomaly, 1 for normal)
df['anomaly'] = model.predict(features)

# Save the results
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("✅ Anomaly detection complete and results saved to:", output_path)
