import smtplib
from email.message import EmailMessage
import os

def send_summary_email(csv_filepath, severity_stats):
    msg = EmailMessage()
    msg['Subject'] = '🚨 Anomaly Summary Report'
    msg['From'] = 'bhupendrajogiraj@gmail.com'
    msg['To'] = 'sumukhavasista004@gmail.com'
    msg.set_content(f"""
Hello,

Please find attached the anomaly summary report.

Anomalies by Severity:
- High: {severity_stats.get('high', 0)}
- Medium: {severity_stats.get('medium', 0)}
- Low: {severity_stats.get('low', 0)}

Best regards,
Cyber Threat Detection System
""")

    # Attach the CSV file
    with open(csv_filepath, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='csv', filename=os.path.basename(csv_filepath))

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('bhupendrajogiraj@gmail.com', 'bbjf tzvr hllb hrqj')  # Replace or use env variables
        smtp.send_message(msg)
        print("📧 Summary email sent successfully.")
