from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class IAccountRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, account_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, customer_id: str, account_type: str, balance: float) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, account_id: str, account_type: str, balance: float) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, account_id: str) -> Optional[Dict]:
        pass
