from typing import List, Dict, Optional
from interfaces.employee_repository_interface import IEmployeeRepository

class EmployeeService:
    def __init__(self, employee_repo: IEmployeeRepository):
        self.employee_repo = employee_repo

    async def get_all_employees(self, conn) -> List[Dict]:
        return await self.employee_repo.get_all(conn)

    async def get_employee_by_id(self, conn, employee_id: str) -> Optional[Dict]:
        return await self.employee_repo.get_by_id(conn, employee_id)

    async def create_employee(self, conn, branch_id: str, full_name: str, role: str) -> Dict:
        return await self.employee_repo.create(conn, branch_id, full_name, role)

    async def update_employee(self, conn, employee_id: str, branch_id: str, full_name: str, role: str) -> Optional[Dict]:
        return await self.employee_repo.update(conn, employee_id, branch_id, full_name, role)

    async def delete_employee(self, conn, employee_id: str) -> Optional[Dict]:
        return await self.employee_repo.delete(conn, employee_id)
