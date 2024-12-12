from typing import List, Dict, Optional
from interfaces.atm_repository_interface import IAtmRepository

class AtmsRepository(IAtmRepository):
    def __init__(self):
        self.select_all_query = "SELECT * FROM atms;"
        self.select_by_id_query = "SELECT * FROM atms WHERE atm_id=$1;"
        self.insert_query = "INSERT INTO atms (location, status) VALUES ($1, $2) RETURNING *;"
        self.update_query = "UPDATE atms SET location=$2, status=$3 WHERE atm_id=$1 RETURNING *;"
        self.delete_query = "DELETE FROM atms WHERE atm_id=$1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, atm_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, atm_id)
        return dict(row) if row else None

    async def create(self, conn, location: str, status: str) -> Dict:
        row = await conn.fetchrow(self.insert_query, location, status)
        return dict(row) if row else {}

    async def update(self, conn, atm_id: str, location: str, status: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.update_query, atm_id, location, status)
        return dict(row) if row else None

    async def delete(self, conn, atm_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, atm_id)
        return dict(row) if row else None
