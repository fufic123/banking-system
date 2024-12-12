from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class ITransactionRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, transaction_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, account_id: str, amount: float, transaction_type: str,
                     performed_via: str, atm_id: Optional[str], branch_id: Optional[str],
                     destination_account_id: Optional[str]) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, transaction_id: str, account_id: str, amount: float,
                     transaction_type: str, performed_via: str, atm_id: Optional[str],
                     branch_id: Optional[str], destination_account_id: Optional[str]) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, transaction_id: str) -> Optional[Dict]:
        pass
