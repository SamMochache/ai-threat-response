from fastapi import APIRouter
from models import LogEntry
import json
from datetime import datetime
import os

router = APIRouter()

LOG_FILE = "logs/events.jsonl"
os.makedirs("logs", exist_ok=True)

@router.post("/log")
def receive_log(entry: LogEntry):
    log_line = entry.model_dump()
    log_line["received_at"] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_line) + "\n")
    return {"status": "received", "log": log_line}

@router.get("/alerts")
def get_alerts():
    # For now return dummy alert (later AI-generated)
    return {
        "alerts": [
            {
                "id": 1,
                "type": "Brute Force",
                "source_ip": "192.168.1.5",
                "action": "Blocked",
                "time": datetime.utcnow().isoformat()
            }
        ]
    }
