from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class IBranchRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, branch_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, address: str, city: str, state: str) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, branch_id: str, address: str, city: str, state: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, branch_id: str) -> Optional[Dict]:
        pass
