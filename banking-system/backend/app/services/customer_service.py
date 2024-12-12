from typing import List, Dict, Optional
from interfaces.customer_repository_interface import ICustomerRepository

class CustomerService:
    def __init__(self, customer_repo: ICustomerRepository):
        self.customer_repo = customer_repo

    async def get_all_customers(self, conn) -> List[Dict]:
        return await self.customer_repo.get_all(conn)

    async def get_customer_by_id(self, conn, customer_id: str) -> Optional[Dict]:
        return await self.customer_repo.get_by_id(conn, customer_id)

    async def create_customer(self, conn, full_name: str, email: str, phone: str) -> Dict:
        return await self.customer_repo.create(conn, full_name, email, phone)

    async def update_customer(self, conn, customer_id: str, full_name: str, email: str, phone: str) -> Optional[Dict]:
        return await self.customer_repo.update(conn, customer_id, full_name, email, phone)

    async def delete_customer(self, conn, customer_id: str) -> Optional[Dict]:
        return await self.customer_repo.delete(conn, customer_id)
