import pathlib
from typing import List, Dict, Optional
from interfaces.customer_repository_interface import ICustomerRepository

class CustomersRepository(ICustomerRepository):
    def __init__(self):
        base_path = pathlib.Path(__file__).parent.parent / 'queries' / 'customers.sql'
        text = base_path.read_text()
        # We'll store queries directly:
        # We know the order from the file:
        # SELECT ALL, SELECT BY ID, INSERT, UPDATE, DELETE
        lines = [line.strip() for line in text.split('\n') if line.strip() and not line.strip().startswith('--')]
        # Given the file:
        # 1: SELECT * FROM customers;
        # 2: SELECT * FROM customers WHERE customer_id = $1;
        # 3: INSERT ...
        # 4: UPDATE ...
        # 5: DELETE ...
        # We'll just hardcode final queries since we know them:
        self.select_all_query = "SELECT * FROM customers;"
        self.select_by_id_query = "SELECT * FROM customers WHERE customer_id = $1;"
        self.insert_query = "INSERT INTO customers (full_name, email, phone) VALUES ($1, $2, $3) RETURNING *;"
        self.update_query = "UPDATE customers SET full_name = $2, email = $3, phone = $4 WHERE customer_id = $1 RETURNING *;"
        self.delete_query = "DELETE FROM customers WHERE customer_id = $1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, customer_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, customer_id)
        return dict(row) if row else None

    async def create(self, conn, full_name: str, email: str, phone: str) -> Dict:
        row = await conn.fetchrow(self.insert_query, full_name, email, phone)
        return dict(row) if row else {}

    async def update(self, conn, customer_id: str, full_name: str, email: str, phone: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.update_query, customer_id, full_name, email, phone)
        return dict(row) if row else None

    async def delete(self, conn, customer_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, customer_id)
        return dict(row) if row else None
