# AWS Cost Alert - Project 5 🚨💰

This project monitors AWS daily costs using the Cost Explorer API and sends alerts when costs exceed a defined threshold. Alerts are forwarded to **Prometheus Alertmanager**.

## 📌 Features

- Fetches daily unblended AWS costs from the last 7 days.
- Alerts when cost exceeds a customizable threshold (default: $5.00).
- Sends alerts to Alertmanager using HTTP POST requests.
- Uses Python and Boto3 (AWS SDK).
- Easily configurable and extendable.

## 🧰 Tools & Technologies

- **AWS Cost Explorer API**
- **Python 3**
- **Boto3**
- **Alertmanager**
- **Requests Library**

## 📦 Prerequisites

- AWS credentials configured (`~/.aws/credentials` or via environment).
- Alertmanager running locally (`http://localhost:9093`).
- Python 3 installed.
- `requests` and `boto3` libraries installed.

Install Python dependencies:

```bash
pip install boto3 requests pytz
🛠️ How It Works
Defines a time window for the last 7 days.

Uses Boto3 to query AWS Cost Explorer for daily UnblendedCost data.

Compares each day's cost with a set threshold.

If any cost exceeds the threshold, it sends a POST request to Alertmanager.

🚀 Running the Script
bash

python fetch_costs.py

📝 Output Example
pgsql
Date: 2025-05-01, Cost: $0.00
Date: 2025-05-02, Cost: $7.15
⚠️ High AWS cost on 2025-05-02: $7.15
Alert sent! Status code: 200
🧠 Customization
You can change the threshold by editing:

COST_THRESHOLD = 5.0
You can also replace the Alertmanager URL in:
requests.post("http://localhost:9093/api/v1/alerts", json=alert)
📂 Project Structure
bash
Copy
Edit
aws-cost-alert-project5/
│
├── fetch_costs.py       # Main script
├── README.md            # Documentation
📬 Author
Omerofficial
GitHub: github.com/Omerofficial

🚧 Project 5 - Part of DevOps Internship at Elevate Labs.


