from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class StatusOptions(str, Enum):
    Active = "Active"
    Inactive = "Inactive"


class MemberCreateInput(BaseModel):
    first_name: str
    last_name: str
    cpf: str
    email: str
    password: str
    zip: str
    birthday: Optional[datetime] = None
    street: Optional[str] = None  # todo: get from Zip Code
    number: Optional[str] = None
    district: Optional[str] = None  # todo: get from Zip Code
    city: Optional[str] = None  # todo: get from Zip Code
    state: Optional[str] = None  # todo: get from Zip Code
    country: Optional[str] = None  # todo: get from Zip Code
    has_children: Optional[bool] = None
    children_qty: Optional[int] = None
    children_names: Optional[str] = None
    marital_state: Optional[str] = None
    status: Optional[StatusOptions] = StatusOptions.Active
    created_at: Optional[datetime] = datetime.now()
    # Events = backref events


class MemberListOutput(BaseModel):
    member_id: int
    first_name: str
    last_name: str
    cpf: str
    email: str

    class Config:
        orm_mode = True
