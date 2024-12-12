from pydantic import BaseModel
from typing import Optional
from datetime import date

class Card(BaseModel):
    card_id: str
    customer_id: str
    card_number: str
    pin: str
    expiration_date: date
    active: bool

class CardCreate(BaseModel):
    customer_id: str
    card_number: str
    pin: str
    expiration_date: date
    active: bool = True

class CardUpdate(BaseModel):
    card_number: str
    pin: str
    expiration_date: date
    active: bool
