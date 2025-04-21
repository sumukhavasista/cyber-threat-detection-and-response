import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Path to the anomaly output file
input_path = os.path.join('..', 'data', 'output', 'anomaly_output.csv')

# Load the data
df = pd.read_csv(input_path)

# Drop non-numeric columns if any (safety check)
df_numeric = df.select_dtypes(include=['float64', 'int64'])

# Make sure 'anomaly' is in the DataFrame
if 'anomaly' not in df.columns:
    raise ValueError("❌ 'anomaly' column not found in dataset.")

# Pick the first two numeric features that are NOT 'anomaly' or 'anomaly_score'
feature_candidates = [col for col in df_numeric.columns if col not in ['anomaly', 'anomaly_score']]

if len(feature_candidates) < 2:
    raise ValueError("❌ Not enough numeric columns to plot.")

feature_x = feature_candidates[0]
feature_y = feature_candidates[1]

# Plot
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df,
    x=feature_x,
    y=feature_y,
    hue='anomaly',
    palette={1: 'green', -1: 'red'},
    alpha=0.7
)

plt.title(f"Anomaly Detection: {feature_x} vs {feature_y}")
plt.xlabel(feature_x)
plt.ylabel(feature_y)
plt.legend(title="Anomaly")
plt.grid(True)
plt.tight_layout()
plt.show()
