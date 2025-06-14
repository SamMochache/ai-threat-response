import json
import random
from datetime import datetime, timedelta

IP_POOL = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "10.0.0.5"]
EVENTS = ["login_attempt", "file_access", "port_scan", "malware_exec"]
DESCRIPTIONS = {
    "login_attempt": ["Login success", "Login failed", "Multiple failures"],
    "file_access": ["Accessed normal file", "Tried restricted file"],
    "port_scan": ["Port scan detected", "Normal network ping"],
    "malware_exec": ["Malicious executable detected", "Clean execution"]
}

def generate_log(is_malicious=False):
    event = random.choice(EVENTS)
    if is_malicious:
        desc = DESCRIPTIONS[event][-1]  # Pick last one = suspicious
    else:
        desc = DESCRIPTIONS[event][0]  # Pick first one = safe

    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 300))).isoformat(),
        "source_ip": random.choice(IP_POOL),
        "destination_ip": "192.168.100.1",
        "event_type": event,
        "description": desc,
        "label": int(is_malicious)  # 1 = malicious, 0 = normal
    }

with open("ml_logs.jsonl", "w") as f:
    for _ in range(250):  # Normal logs
        f.write(json.dumps(generate_log(False)) + "\n")
    for _ in range(250):  # Malicious logs
        f.write(json.dumps(generate_log(True)) + "\n")

print("✅ Synthetic data generated in ml_logs.jsonl")
