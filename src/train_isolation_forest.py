import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Set paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "final_cleaned_system_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "isolation_forest_model.pkl")

# Load the preprocessed dataset
df = pd.read_csv(DATA_PATH)

# Optional: Drop timestamp column if it exists
if 'timestamp' in df.columns:
    df = df.drop(columns=['timestamp'])

# Train Isolation Forest
model = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
model.fit(df)

# Save the trained model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)

print("✅ Model trained and saved successfully at:", MODEL_PATH)
