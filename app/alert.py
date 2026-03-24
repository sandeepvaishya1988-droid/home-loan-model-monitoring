import requests

def send_slack_alert(message):
    webhook = "YOUR_SLACK_WEBHOOK"
    requests.post(webhook, json={"text": message})
