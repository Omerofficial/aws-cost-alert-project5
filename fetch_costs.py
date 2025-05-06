import boto3
from datetime import datetime, timedelta
import requests
import pytz

# Set your cost threshold (e.g., $5.00)
COST_THRESHOLD = 5.0

# Initialize client
client = boto3.client('ce')

# Set date range using timezone-aware datetime
utc_now = datetime.now(pytz.UTC)
end_date = utc_now.date()
start_date = end_date - timedelta(days=7)

# Call AWS Cost Explorer
try:
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': str(start_date),
            'End': str(end_date)
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    print("AWS Cost Explorer response fetched successfully.")
except Exception as e:
    print(f"Error fetching AWS cost data: {e}")
    exit()

# Function to send alerts to Alertmanager
def send_alert_to_alertmanager(message):
    alert = [{
        "labels": {
            "alertname": "AWSCostAlert",
            "severity": "critical"
        },
        "annotations": {
            "summary": message
        }
    }]
    
    try:
        response = requests.post("http://localhost:9093/api/v1/alerts", json=alert)
        print(f"Alert sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Process response and check cost
for day in response['ResultsByTime']:
    amount = day['Total']['UnblendedCost']['Amount']
    date = day['TimePeriod']['Start']
    print(f"Date: {date}, Cost: ${amount}")

    if float(amount) >= COST_THRESHOLD:
        message = f"⚠️ High AWS cost on {date}: ${amount}"
        send_alert_to_alertmanager(message)
