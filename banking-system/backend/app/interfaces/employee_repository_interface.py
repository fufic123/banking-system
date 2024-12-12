from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class IEmployeeRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, employee_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, branch_id: str, full_name: str, role: str) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, employee_id: str, branch_id: str, full_name: str, role: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, employee_id: str) -> Optional[Dict]:
        pass
