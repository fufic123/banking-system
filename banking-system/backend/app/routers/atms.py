from fastapi import APIRouter, Depends
from db import get_db_connection
from repositories.atms_repo import AtmsRepository
from services.atm_service import AtmService
from models.atm_model import AtmCreate, AtmUpdate

router = APIRouter(prefix="/atms", tags=["atms"])
atm_repo = AtmsRepository()
atm_service = AtmService(atm_repo)

@router.get("/")
async def list_atms(conn=Depends(get_db_connection)):
    return await atm_service.get_all_atms(conn)

@router.get("/{atm_id}")
async def get_atm(atm_id: str, conn=Depends(get_db_connection)):
    atm = await atm_service.get_atm_by_id(conn, atm_id)
    if atm:
        return atm
    return {"error": "ATM not found"}

@router.post("/")
async def create_atm(payload: AtmCreate, conn=Depends(get_db_connection)):
    new_atm = await atm_service.create_atm(conn, payload.location, payload.status)
    return new_atm

@router.put("/{atm_id}")
async def update_atm(atm_id: str, payload: AtmUpdate, conn=Depends(get_db_connection)):
    updated = await atm_service.update_atm(conn, atm_id, payload.location, payload.status)
    if updated:
        return updated
    return {"error": "ATM not found"}

@router.delete("/{atm_id}")
async def delete_atm(atm_id: str, conn=Depends(get_db_connection)):
    deleted = await atm_service.delete_atm(conn, atm_id)
    if deleted:
        return deleted
    return {"error": "ATM not found"}
