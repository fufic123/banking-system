from fastapi import APIRouter, Depends
from db import get_db_connection
from repositories.employees_repo import EmployeesRepository
from services.employee_service import EmployeeService
from models.employee_model import EmployeeCreate, EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["employees"])
employee_repo = EmployeesRepository()
employee_service = EmployeeService(employee_repo)

@router.get("/")
async def list_employees(conn=Depends(get_db_connection)):
    return await employee_service.get_all_employees(conn)

@router.get("/{employee_id}")
async def get_employee(employee_id: str, conn=Depends(get_db_connection)):
    emp = await employee_service.get_employee_by_id(conn, employee_id)
    if emp:
        return emp
    return {"error": "Employee not found"}

@router.post("/")
async def create_employee(payload: EmployeeCreate, conn=Depends(get_db_connection)):
    new_emp = await employee_service.create_employee(conn, payload.branch_id, payload.full_name, payload.role)
    return new_emp

@router.put("/{employee_id}")
async def update_employee(employee_id: str, payload: EmployeeUpdate, conn=Depends(get_db_connection)):
    updated = await employee_service.update_employee(conn, employee_id, payload.branch_id, payload.full_name, payload.role)
    if updated:
        return updated
    return {"error": "Employee not found"}

@router.delete("/{employee_id}")
async def delete_employee(employee_id: str, conn=Depends(get_db_connection)):
    deleted = await employee_service.delete_employee(conn, employee_id)
    if deleted:
        return deleted
    return {"error": "Employee not found"}
