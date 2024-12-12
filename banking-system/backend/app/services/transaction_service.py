from typing import List, Dict, Optional
from interfaces.transaction_repository_interface import ITransactionRepository

class TransactionService:
    def __init__(self, transaction_repo: ITransactionRepository):
        self.transaction_repo = transaction_repo

    async def get_all_transactions(self, conn) -> List[Dict]:
        return await self.transaction_repo.get_all(conn)

    async def get_transaction_by_id(self, conn, transaction_id: str) -> Optional[Dict]:
        return await self.transaction_repo.get_by_id(conn, transaction_id)

    async def create_transaction(self, conn, account_id: str, amount: float, transaction_type: str,
                                 performed_via: str, atm_id: Optional[str], branch_id: Optional[str],
                                 destination_account_id: Optional[str]) -> Dict:
        return await self.transaction_repo.create(conn, account_id, amount, transaction_type, performed_via, atm_id, branch_id, destination_account_id)

    async def update_transaction(self, conn, transaction_id: str, account_id: str, amount: float,
                                 transaction_type: str, performed_via: str, atm_id: Optional[str],
                                 branch_id: Optional[str], destination_account_id: Optional[str]) -> Optional[Dict]:
        return await self.transaction_repo.update(conn, transaction_id, account_id, amount, transaction_type, performed_via, atm_id, branch_id, destination_account_id)

    async def delete_transaction(self, conn, transaction_id: str) -> Optional[Dict]:
        return await self.transaction_repo.delete(conn, transaction_id)
