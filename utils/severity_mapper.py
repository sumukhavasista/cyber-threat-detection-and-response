import numpy as np
import pandas as pd

def apply_dynamic_severity(df: pd.DataFrame, score_column: str = 'scores', label_column: str = 'anomaly') -> pd.DataFrame:
    """
    Adds a 'severity' column to the DataFrame based on dynamic percentile thresholds.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing anomaly scores and labels.
        score_column (str): Name of the column with anomaly scores.
        label_column (str): Name of the column with anomaly labels (-1 for anomaly, 1 for normal).

    Returns:
        pd.DataFrame: DataFrame with an added 'severity' column.
    """
    # Step 2: Compute thresholds
    p95 = np.percentile(df[score_column], 95)
    p85 = np.percentile(df[score_column], 85)
    p70 = np.percentile(df[score_column], 70)

    # Step 3: Define severity mapping function
    def map_severity(score):
        if score < p95:
            return "Critical"
        elif score < p85:
            return "High"
        elif score < p70:
            return "Medium"
        else:
            return "Low"

    # Step 4: Apply severity mapping
    df['severity'] = df[score_column].apply(map_severity)

    # Optional: Keep 'Normal' for non-anomalies
    df['severity'] = df.apply(lambda row: row['severity'] if row[label_column] == -1 else "Normal", axis=1)

    return df
