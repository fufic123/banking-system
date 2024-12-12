from typing import List, Dict, Optional
from interfaces.branch_repository_interface import IBranchRepository

class BranchService:
    def __init__(self, branch_repo: IBranchRepository):
        self.branch_repo = branch_repo

    async def get_all_branches(self, conn) -> List[Dict]:
        return await self.branch_repo.get_all(conn)

    async def get_branch_by_id(self, conn, branch_id: str) -> Optional[Dict]:
        return await self.branch_repo.get_by_id(conn, branch_id)

    async def create_branch(self, conn, address: str, city: str, state: str) -> Dict:
        return await self.branch_repo.create(conn, address, city, state)

    async def update_branch(self, conn, branch_id: str, address: str, city: str, state: str) -> Optional[Dict]:
        return await self.branch_repo.update(conn, branch_id, address, city, state)

    async def delete_branch(self, conn, branch_id: str) -> Optional[Dict]:
        return await self.branch_repo.delete(conn, branch_id)
