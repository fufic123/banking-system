from pydantic import BaseModel

class Atm(BaseModel):
    atm_id: str
    location: str
    status: str

class AtmCreate(BaseModel):
    location: str
    status: str = "operational"

class AtmUpdate(BaseModel):
    location: str
    status: str
