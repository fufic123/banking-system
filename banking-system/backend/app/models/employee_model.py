from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: str
    branch_id: str
    full_name: str
    role: str

class EmployeeCreate(BaseModel):
    branch_id: str
    full_name: str
    role: str

class EmployeeUpdate(BaseModel):
    branch_id: str
    full_name: str
    role: str
