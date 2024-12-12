from typing import List, Dict, Optional
from interfaces.transaction_repository_interface import ITransactionRepository

class TransactionsRepository(ITransactionRepository):
    def __init__(self):
        self.select_all_query = "SELECT * FROM transactions;"
        self.select_by_id_query = "SELECT * FROM transactions WHERE transaction_id=$1;"
        self.insert_query = """
            INSERT INTO transactions (account_id, amount, transaction_type, performed_via, atm_id, branch_id, destination_account_id)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING *;
        """

        self.update_query = """
            UPDATE transactions
            SET account_id = $2,
                amount = $3,
                transaction_type = $4,
                performed_via = $5,
                atm_id = $6,
                branch_id = $7,
                destination_account_id = $8,
                performed_at = NOW()
            WHERE transaction_id = $1
            RETURNING *;
        """

        self.delete_query = "DELETE FROM transactions WHERE transaction_id=$1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, transaction_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, transaction_id)
        return dict(row) if row else None

    async def create(self, conn, account_id: str, amount: float, transaction_type: str,
                     performed_via: str, atm_id: Optional[str], branch_id: Optional[str],
                     destination_account_id: Optional[str]) -> Dict:
        row = await conn.fetchrow(
            self.insert_query,
            account_id, amount, transaction_type, performed_via, atm_id, branch_id, destination_account_id
        )
        return dict(row) if row else {}

    async def update(self, conn, transaction_id: str, account_id: str, amount: float,
                     transaction_type: str, performed_via: str, atm_id: Optional[str],
                     branch_id: Optional[str], destination_account_id: Optional[str]) -> Optional[Dict]:
        row = await conn.fetchrow(
            self.update_query,
            transaction_id, account_id, amount, transaction_type, performed_via, atm_id, branch_id, destination_account_id
        )
        return dict(row) if row else None

    async def delete(self, conn, transaction_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, transaction_id)
        return dict(row) if row else None
