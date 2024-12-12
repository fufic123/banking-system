from typing import List, Dict, Optional
from interfaces.employee_repository_interface import IEmployeeRepository

class EmployeesRepository(IEmployeeRepository):
    def __init__(self):
        self.select_all_query = "SELECT * FROM employees;"
        self.select_by_id_query = "SELECT * FROM employees WHERE employee_id=$1;"
        self.insert_query = "INSERT INTO employees (branch_id, full_name, role) VALUES ($1, $2, $3) RETURNING *;"
        self.update_query = "UPDATE employees SET branch_id=$2, full_name=$3, role=$4 WHERE employee_id=$1 RETURNING *;"
        self.delete_query = "DELETE FROM employees WHERE employee_id=$1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, employee_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, employee_id)
        return dict(row) if row else None

    async def create(self, conn, branch_id: str, full_name: str, role: str) -> Dict:
        row = await conn.fetchrow(self.insert_query, branch_id, full_name, role)
        return dict(row) if row else {}

    async def update(self, conn, employee_id: str, branch_id: str, full_name: str, role: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.update_query, employee_id, branch_id, full_name, role)
        return dict(row) if row else None

    async def delete(self, conn, employee_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, employee_id)
        return dict(row) if row else None
