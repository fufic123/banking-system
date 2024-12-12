from fastapi import APIRouter, Depends
from typing import Optional
from datetime import date
from db import get_db_connection
from repositories.cards_repo import CardsRepository
from services.card_service import CardService
from models.card_model import CardCreate, CardUpdate

router = APIRouter(prefix="/cards", tags=["cards"])
card_repo = CardsRepository()
card_service = CardService(card_repo)

@router.get("/")
async def list_cards(conn=Depends(get_db_connection)):
    return await card_service.get_all_cards(conn)

@router.get("/{card_id}")
async def get_card(card_id: str, conn=Depends(get_db_connection)):
    card = await card_service.get_card_by_id(conn, card_id)
    if card:
        return card
    return {"error": "Card not found"}

@router.post("/")
async def create_card(payload: CardCreate, conn=Depends(get_db_connection)):
    new_card = await card_service.create_card(conn, payload.customer_id, payload.card_number, payload.pin, payload.expiration_date, payload.active)
    return new_card

@router.put("/{card_id}")
async def update_card(card_id: str, payload: CardUpdate, conn=Depends(get_db_connection)):
    updated = await card_service.update_card(conn, card_id, payload.card_number, payload.pin, payload.expiration_date, payload.active)
    if updated:
        return updated
    return {"error": "Card not found"}

@router.delete("/{card_id}")
async def delete_card(card_id: str, conn=Depends(get_db_connection)):
    deleted = await card_service.delete_card(conn, card_id)
    if deleted:
        return deleted
    return {"error": "Card not found"}
