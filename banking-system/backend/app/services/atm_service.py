from typing import List, Dict, Optional
from interfaces.atm_repository_interface import IAtmRepository

class AtmService:
    def __init__(self, atm_repo: IAtmRepository):
        self.atm_repo = atm_repo

    async def get_all_atms(self, conn) -> List[Dict]:
        return await self.atm_repo.get_all(conn)

    async def get_atm_by_id(self, conn, atm_id: str) -> Optional[Dict]:
        return await self.atm_repo.get_by_id(conn, atm_id)

    async def create_atm(self, conn, location: str, status: str) -> Dict:
        return await self.atm_repo.create(conn, location, status)

    async def update_atm(self, conn, atm_id: str, location: str, status: str) -> Optional[Dict]:
        return await self.atm_repo.update(conn, atm_id, location, status)

    async def delete_atm(self, conn, atm_id: str) -> Optional[Dict]:
        return await self.atm_repo.delete(conn, atm_id)
