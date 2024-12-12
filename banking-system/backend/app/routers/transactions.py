from fastapi import APIRouter, Depends, HTTPException
from db import get_db_connection
from repositories.transactions_repo import TransactionsRepository
from services.transaction_service import TransactionService
from models.transaction_model import TransactionCreate, TransactionUpdate

router = APIRouter(prefix="/transactions", tags=["transactions"])
transaction_repo = TransactionsRepository()
transaction_service = TransactionService(transaction_repo)

@router.get("/")
async def list_transactions(conn=Depends(get_db_connection)):
    return await transaction_service.get_all_transactions(conn)

@router.get("/{transaction_id}")
async def get_transaction(transaction_id: str, conn=Depends(get_db_connection)):
    tx = await transaction_service.get_transaction_by_id(conn, transaction_id)
    if tx:
        return tx
    raise HTTPException(status_code=404, detail="Transaction not found")

@router.post("/")
async def create_transaction(payload: TransactionCreate, conn=Depends(get_db_connection)):
    new_tx = await transaction_service.create_transaction(
        conn,
        str(payload.account_id),
        payload.amount,
        payload.transaction_type,
        payload.performed_via,
        str(payload.atm_id) if payload.atm_id else None,
        str(payload.branch_id) if payload.branch_id else None,
        str(payload.destination_account_id) if payload.destination_account_id else None
    )
    return new_tx

@router.put("/{transaction_id}")
async def update_transaction(transaction_id: str, payload: TransactionUpdate, conn=Depends(get_db_connection)):
    updated = await transaction_service.update_transaction(
        conn,
        transaction_id,
        str(payload.account_id),
        payload.amount,
        payload.transaction_type,
        payload.performed_via,
        str(payload.atm_id) if payload.atm_id else None,
        str(payload.branch_id) if payload.branch_id else None,
        str(payload.destination_account_id) if payload.destination_account_id else None
    )
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Transaction not found")

@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: str, conn=Depends(get_db_connection)):
    deleted = await transaction_service.delete_transaction(conn, transaction_id)
    if deleted:
        return deleted
    raise HTTPException(status_code=404, detail="Transaction not found")
