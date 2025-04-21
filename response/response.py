import pandas as pd
from .email_notifier import send_summary_email
from .dashboard_logger import log_to_dashboard
from .containment_actions import perform_containment_action
from severity_mapper import determine_severity

collected_anomalies = []

def collect_anomaly(anomaly_row):
    collected_anomalies.append(anomaly_row)

def finalize_response():
    if not collected_anomalies:
        print("✅ No anomalies to respond to.")
        return

    df = pd.DataFrame(collected_anomalies)

    if 'severity' not in df.columns:
        df['severity'] = df.apply(determine_severity, axis=1)

    # Save CSV
    csv_path = "anomaly_summary.csv"
    df.to_csv(csv_path, index=False)

    # Calculate severity statistics for summary
    severity_stats = df['severity'].value_counts().to_dict()

    # Trigger responses
    send_summary_email(csv_path, severity_stats)
    log_to_dashboard(csv_path)

    for _, row in df.iterrows():
        action_type = row.get("containment_action", "isolate_system")  # default if not provided
        details = row.get("system_id", "Unknown")
        perform_containment_action(action_type, details)