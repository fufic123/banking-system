from fastapi import APIRouter, Depends
from db import get_db_connection
from repositories.branches_repo import BranchesRepository
from services.branch_service import BranchService
from models.branch_model import BranchCreate, BranchUpdate

router = APIRouter(prefix="/branches", tags=["branches"])
branch_repo = BranchesRepository()
branch_service = BranchService(branch_repo)

@router.get("/")
async def list_branches(conn=Depends(get_db_connection)):
    return await branch_service.get_all_branches(conn)

@router.get("/{branch_id}")
async def get_branch(branch_id: str, conn=Depends(get_db_connection)):
    branch = await branch_service.get_branch_by_id(conn, branch_id)
    if branch:
        return branch
    return {"error": "Branch not found"}

@router.post("/")
async def create_branch(payload: BranchCreate, conn=Depends(get_db_connection)):
    new_branch = await branch_service.create_branch(conn, payload.address, payload.city, payload.state)
    return new_branch

@router.put("/{branch_id}")
async def update_branch(branch_id: str, payload: BranchUpdate, conn=Depends(get_db_connection)):
    updated = await branch_service.update_branch(conn, branch_id, payload.address, payload.city, payload.state)
    if updated:
        return updated
    return {"error": "Branch not found"}

@router.delete("/{branch_id}")
async def delete_branch(branch_id: str, conn=Depends(get_db_connection)):
    deleted = await branch_service.delete_branch(conn, branch_id)
    if deleted:
        return deleted
    return {"error": "Branch not found"}
