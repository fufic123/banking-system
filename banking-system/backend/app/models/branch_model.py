from pydantic import BaseModel

class Branch(BaseModel):
    branch_id: str
    address: str
    city: str
    state: str

class BranchCreate(BaseModel):
    address: str
    city: str
    state: str

class BranchUpdate(BaseModel):
    address: str
    city: str
    state: str
