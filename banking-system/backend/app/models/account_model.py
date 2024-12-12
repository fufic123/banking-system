from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Account(BaseModel):
    account_id: str
    customer_id: str
    account_type: str
    balance: float
    created_at: datetime

class AccountCreate(BaseModel):
    customer_id: str
    account_type: str
    balance: float

class AccountUpdate(BaseModel):
    account_type: str
    balance: float
