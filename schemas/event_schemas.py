from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime


class StatusOptions(str, Enum):
    Active = "Active"
    Inactive = "Inactive"


class EventCreateInput(BaseModel):

    member_id: int
    type: str
    date: date
    start_time: time
    end_time: time
    warned_peers: bool
    warned_team: bool
    warned_leader: bool
    defined_substitute: bool
    substitute: str
    pending_task: bool
    document: Optional[bytes] = None
    created_at: Optional[datetime] = datetime.now()
    status: Optional[StatusOptions] = StatusOptions.Active
