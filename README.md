# AI-Powered Cyber Threat Detection and Response

An intelligent system designed to detect anomalies in system performance data using machine learning and trigger automated response mechanisms such as email alerts, dashboard logging, and simulated containment actions.

## 🚀 Features

- **Anomaly Detection**: Utilizes the Isolation Forest algorithm to identify unusual patterns in system data.
- **Severity Classification**: Assigns severity levels (High, Medium, Low) to detected anomalies.
- **Summary Email Alerts**: Sends a consolidated email with a CSV attachment detailing all detected anomalies.
- **Dashboard Logging**: Logs anomaly summaries into a timestamped dashboard directory for record-keeping.
- **Simulated Containment Actions**: Mimics response actions like isolating systems or terminating processes based on anomaly severity.

## 📁 Project Structure

cyber-threat-detection-and-response/ 
├── data/ 
    │ └── processed/ 
    │ └── final_cleaned_system_data.csv 
├── models/ 
    │ └── isolation_forest_model.pkl 
├── response/ 
    │ ├── init.py 
    │ ├── response.py 
    │ ├── email_notifier.py 
    │ ├── dashboard_logger.py 
    │ └── containment_actions.py 
├── severity_mapper.py 
├── main.py 
└── anomaly_summary.csv


## 🛠️ Setup & Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sumukhavasista/cyber-threat-detection-and-response.git
   cd cyber-threat-detection-and-response

pip install -r requirements.txt
pip freeze > requirements.txt
