from typing import List, Dict, Optional
from interfaces.branch_repository_interface import IBranchRepository

class BranchesRepository(IBranchRepository):
    def __init__(self):
        self.select_all_query = "SELECT * FROM branches;"
        self.select_by_id_query = "SELECT * FROM branches WHERE branch_id=$1;"
        self.insert_query = "INSERT INTO branches (address, city, state) VALUES ($1, $2, $3) RETURNING *;"
        self.update_query = "UPDATE branches SET address=$2, city=$3, state=$4 WHERE branch_id=$1 RETURNING *;"
        self.delete_query = "DELETE FROM branches WHERE branch_id=$1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, branch_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, branch_id)
        return dict(row) if row else None

    async def create(self, conn, address: str, city: str, state: str) -> Dict:
        row = await conn.fetchrow(self.insert_query, address, city, state)
        return dict(row) if row else {}

    async def update(self, conn, branch_id: str, address: str, city: str, state: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.update_query, branch_id, address, city, state)
        return dict(row) if row else None

    async def delete(self, conn, branch_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, branch_id)
        return dict(row) if row else None
