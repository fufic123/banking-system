from typing import List, Dict, Optional
from datetime import date
from interfaces.card_repository_interface import ICardRepository
from utils.hashing import hash_pin

class CardService:
    def __init__(self, card_repo: ICardRepository):
        self.card_repo = card_repo

    async def get_all_cards(self, conn) -> List[Dict]:
        return await self.card_repo.get_all(conn)

    async def get_card_by_id(self, conn, card_id: str) -> Optional[Dict]:
        return await self.card_repo.get_by_id(conn, card_id)

    async def create_card(self, conn, customer_id: str, card_number: str, pin: str, expiration_date: date, active: bool) -> Dict:
        # Hash the pin before storing
        hashed = hash_pin(pin)
        return await self.card_repo.create(conn, customer_id, card_number, hashed, expiration_date, active)

    async def update_card(self, conn, card_id: str, card_number: str, pin: str, expiration_date: date, active: bool) -> Optional[Dict]:
        # Hash the pin before updating
        hashed = hash_pin(pin)
        return await self.card_repo.update(conn, card_id, card_number, hashed, expiration_date, active)

    async def delete_card(self, conn, card_id: str) -> Optional[Dict]:
        return await self.card_repo.delete(conn, card_id)
