from fastapi import APIRouter, Depends
from db import get_db_connection
from repositories.accounts_repo import AccountsRepository
from services.account_service import AccountService
from models.account_model import AccountCreate, AccountUpdate

router = APIRouter(prefix="/accounts", tags=["accounts"])
account_repo = AccountsRepository()
account_service = AccountService(account_repo)

@router.get("/")
async def list_accounts(conn=Depends(get_db_connection)):
    return await account_service.get_all_accounts(conn)

@router.get("/{account_id}")
async def get_account(account_id: str, conn=Depends(get_db_connection)):
    acc = await account_service.get_account_by_id(conn, account_id)
    if acc:
        return acc
    return {"error": "Account not found"}

@router.post("/")
async def create_account(payload: AccountCreate, conn=Depends(get_db_connection)):
    new_acc = await account_service.create_account(conn, payload.customer_id, payload.account_type, payload.balance)
    return new_acc

@router.put("/{account_id}")
async def update_account(account_id: str, payload: AccountUpdate, conn=Depends(get_db_connection)):
    updated = await account_service.update_account(conn, account_id, payload.account_type, payload.balance)
    if updated:
        return updated
    return {"error": "Account not found"}

@router.delete("/{account_id}")
async def delete_account(account_id: str, conn=Depends(get_db_connection)):
    deleted = await account_service.delete_account(conn, account_id)
    if deleted:
        return deleted
    return {"error": "Account not found"}
