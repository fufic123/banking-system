from typing import List, Dict, Optional
from datetime import date
from interfaces.card_repository_interface import ICardRepository

class CardsRepository(ICardRepository):
    def __init__(self):
        self.select_all_query = "SELECT * FROM cards;"
        self.select_by_id_query = "SELECT * FROM cards WHERE card_id=$1;"
        self.insert_query = "INSERT INTO cards (customer_id, card_number, pin, expiration_date, active) VALUES ($1, $2, $3, $4, $5) RETURNING *;"
        self.update_query = "UPDATE cards SET card_number=$2, pin=$3, expiration_date=$4, active=$5 WHERE card_id=$1 RETURNING *;"
        self.delete_query = "DELETE FROM cards WHERE card_id=$1 RETURNING *;"

    async def get_all(self, conn) -> List[Dict]:
        rows = await conn.fetch(self.select_all_query)
        return [dict(r) for r in rows]

    async def get_by_id(self, conn, card_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.select_by_id_query, card_id)
        return dict(row) if row else None

    async def create(self, conn, customer_id: str, card_number: str, pin: str, expiration_date: date, active: bool) -> Dict:
        row = await conn.fetchrow(self.insert_query, customer_id, card_number, pin, expiration_date, active)
        return dict(row) if row else {}

    async def update(self, conn, card_id: str, card_number: str, pin: str, expiration_date: date, active: bool) -> Optional[Dict]:
        row = await conn.fetchrow(self.update_query, card_id, card_number, pin, expiration_date, active)
        return dict(row) if row else None

    async def delete(self, conn, card_id: str) -> Optional[Dict]:
        row = await conn.fetchrow(self.delete_query, card_id)
        return dict(row) if row else None
