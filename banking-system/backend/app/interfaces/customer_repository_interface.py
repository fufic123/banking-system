from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class ICustomerRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, customer_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, full_name: str, email: str, phone: str) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, customer_id: str, full_name: str, email: str, phone: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, customer_id: str) -> Optional[Dict]:
        pass
