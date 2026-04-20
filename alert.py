import requests
import os


DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(alert):
    payload = {
        "username": "SLO Monitor",
        "embeds": [
            {
                "title": f"[{alert['severity']}] {alert['name']}",
                "color": 15158332 if alert["severity"] == "P1" else 16776960,
                "fields": [
                    {"name": "Metric", "value": alert["metric"], "inline": True},
                    {"name": "Value", "value": str(alert["value"]), "inline": True},
                    {"name": "Threshold", "value": alert["threshold"], "inline": False},
                    {"name": "Owner", "value": alert["owner"], "inline": True},
                ],
                "footer": {"text": "AI Monitoring Demo"},
            }
        ],
    }

    requests.post(DISCORD_WEBHOOK, json=payload)


alert = {
    "severity": "P1",
    "name": "High Error Rate",
    "metric": "error_rate_pct",
    "value": 10,
    "threshold": 5,
    "owner": "team-oncall",
}

send_discord_alert(alert)
