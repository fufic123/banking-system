import pathlib
from typing import List, Dict, Optional
from interfaces.account_repository_interface import IAccountRepository

class AccountsRepository(IAccountRepository):
    def __init__(self):
        self.select_all_query = "SELECT * FROM accounts;"
        self.select_by_id_query = "SELECT * FROM accounts WHERE account_id = $1;"
        self.insert_query = "INSERT INTO accounts (customer_id, account_type, balance) VALUES ($1, $2, $3) RETURNING *;"
        self.update_query = "UPDATE accounts SET account_type = $2, balance = $3 WHERE account_id = $1 RETURNING *;"
        self.delete_query = "DELETE FROM accounts WHERE account_id = $1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, account_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, account_id)
        return dict(row) if row else None

    async def create(self, conn, customer_id: str, account_type: str, balance: float) -> Dict:
        row = await conn.fetchrow(self.insert_query, customer_id, account_type, balance)
        return dict(row) if row else {}

    async def update(self, conn, account_id: str, account_type: str, balance: float) -> Optional[Dict]:
        row = await conn.fetchrow(self.update_query, account_id, account_type, balance)
        return dict(row) if row else None

    async def delete(self, conn, account_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, account_id)
        return dict(row) if row else None
