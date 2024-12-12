from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Customer(BaseModel):
    customer_id: str
    full_name: str
    email: EmailStr
    phone: Optional[str]
    created_at: datetime

class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str]

class CustomerUpdate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str]
