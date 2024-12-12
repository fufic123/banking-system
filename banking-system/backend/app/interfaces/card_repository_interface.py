from abc import ABC, abstractmethod
from typing import Optional, List, Dict
from datetime import date

class ICardRepository(ABC):
    @abstractmethod
    async def get_all(self, conn) -> List[Dict]:
        pass

    @abstractmethod
    async def get_by_id(self, conn, card_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def create(self, conn, customer_id: str, card_number: str, pin: str, expiration_date: date, active: bool) -> Dict:
        pass

    @abstractmethod
    async def update(self, conn, card_id: str, card_number: str, pin: str, expiration_date: date, active: bool) -> Optional[Dict]:
        pass

    @abstractmethod
    async def delete(self, conn, card_id: str) -> Optional[Dict]:
        pass
