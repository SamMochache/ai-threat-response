from pydantic import BaseModel
from typing import Optional

class LogEntry(BaseModel):
    timestamp: str
    source_ip: str
    destination_ip: str
    event_type: str
    username: Optional[str] = None
    description: Optional[str] = None
