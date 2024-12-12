from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class IAtmRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, atm_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, location: str, status: str) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, atm_id: str, location: str, status: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, atm_id: str) -> Optional[Dict]:
        pass
