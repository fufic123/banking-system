from fastapi import APIRouter, Depends
from db import get_db_connection
from repositories.customers_repo import CustomersRepository
from services.customer_service import CustomerService
from models.customer_model import CustomerCreate, CustomerUpdate

router = APIRouter(prefix="/customers", tags=["customers"])
customer_repo = CustomersRepository()
customer_service = CustomerService(customer_repo)

@router.get("/")
async def list_customers(conn=Depends(get_db_connection)):
    return await customer_service.get_all_customers(conn)

@router.get("/{customer_id}")
async def get_customer(customer_id: str, conn=Depends(get_db_connection)):
    customer = await customer_service.get_customer_by_id(conn, customer_id)
    if customer:
        return customer
    return {"error": "Customer not found"}

@router.post("/")
async def create_customer(payload: CustomerCreate, conn=Depends(get_db_connection)):
    new_customer = await customer_service.create_customer(conn, payload.full_name, payload.email, payload.phone)
    return new_customer

@router.put("/{customer_id}")
async def update_customer(customer_id: str, payload: CustomerUpdate, conn=Depends(get_db_connection)):
    updated = await customer_service.update_customer(conn, customer_id, payload.full_name, payload.email, payload.phone)
    if updated:
        return updated
    return {"error": "Customer not found"}

@router.delete("/{customer_id}")
async def delete_customer(customer_id: str, conn=Depends(get_db_connection)):
    deleted = await customer_service.delete_customer(conn, customer_id)
    if deleted:
        return deleted
    return {"error": "Customer not found"}
