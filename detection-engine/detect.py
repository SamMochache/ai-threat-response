import json
import time
from datetime import datetime
import joblib

LOG_FILE = "../backend/logs/events.jsonl"
ALERTS_FILE = "alerts/alerts.jsonl"

clf = joblib.load("threat_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

seen = set()

def log_alert(alert):
    with open(ALERTS_FILE, "a") as f:
        f.write(json.dumps(alert) + "\n")
    print("[AI ALERT]", alert)

def predict_threat(log):
    text = log["event_type"] + " " + log.get("description", "")
    vec = vectorizer.transform([text])
    return clf.predict(vec)[0] == 1

def detect_with_ml():
    while True:
        try:
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            time.sleep(1)
            continue

        for line in lines:
            if line in seen:
                continue
            seen.add(line)

            try:
                log = json.loads(line)
            except json.JSONDecodeError:
                continue

            if predict_threat(log):
                alert = {
                    "type": "AI Threat Detection",
                    "source_ip": log.get("source_ip"),
                    "description": log.get("description"),
                    "event_type": log.get("event_type"),
                    "time": log.get("timestamp"),
                    "action": "Investigate immediately"
                }
                log_alert(alert)

        time.sleep(2)

if __name__ == "__main__":
    print("🤖 AI Detection Engine Running...")
    detect_with_ml()
