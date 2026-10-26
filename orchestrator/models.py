from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from enum import Enum
import uuid

def now(): return datetime.now(timezone.utc).isoformat()
class State(str, Enum):
    DISCOVERED="DISCOVERED"; RIGHTS_CHECK="RIGHTS_CHECK"; READY="READY"
    PROCESSING="PROCESSING"; VALIDATING="VALIDATING"; READY_TO_PUBLISH="READY_TO_PUBLISH"
    PUBLISHING="PUBLISHING"; PUBLISHED="PUBLISHED"; RETRY_WAIT="RETRY_WAIT"
    REJECTED_RIGHTS="REJECTED_RIGHTS"; FAILED="FAILED"

@dataclass
class Job:
    source_url: str
    source_kind: str = "upload"
    job_id: str = ""
    state: str = State.DISCOVERED.value
    output_format: str = "short"
    channel_id: str = ""
    source_license: str = ""
    license_url: str = ""
    creator: str = ""
    attribution: str = ""
    rights_evidence: str = ""
    output_key: str = ""
    youtube_video_id: str = ""
    attempts: int = 0
    last_error: str = ""
    created_at: str = ""
    updated_at: str = ""
    def __post_init__(self):
        self.job_id = self.job_id or str(uuid.uuid4())
        self.created_at = self.created_at or now()
        self.updated_at = now()
    def to_dict(self): return asdict(self)
