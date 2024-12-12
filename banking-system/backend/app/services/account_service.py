from typing import List, Dict, Optional
from interfaces.account_repository_interface import IAccountRepository

class AccountService:
    def __init__(self, account_repo: IAccountRepository):
        self.account_repo = account_repo

    async def get_all_accounts(self, conn) -> List[Dict]:
        return await self.account_repo.get_all(conn)

    async def get_account_by_id(self, conn, account_id: str) -> Optional[Dict]:
        return await self.account_repo.get_by_id(conn, account_id)

    async def create_account(self, conn, customer_id: str, account_type: str, balance: float) -> Dict:
        return await self.account_repo.create(conn, customer_id, account_type, balance)

    async def update_account(self, conn, account_id: str, account_type: str, balance: float) -> Optional[Dict]:
        return await self.account_repo.update(conn, account_id, account_type, balance)

    async def delete_account(self, conn, account_id: str) -> Optional[Dict]:
        return await self.account_repo.delete(conn, account_id)
