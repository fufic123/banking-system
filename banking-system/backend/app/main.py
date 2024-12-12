from fastapi import FastAPI
from .routers.customers import router as customers_router
from .routers.accounts import router as accounts_router
from .routers.cards import router as cards_router
from .routers.atms import router as atms_router
from .routers.branches import router as branches_router
from .routers.employees import router as employees_router
from .routers.transactions import router as transactions_router

app = FastAPI()

app.include_router(customers_router)
app.include_router(accounts_router)
app.include_router(cards_router)
app.include_router(atms_router)
app.include_router(branches_router)
app.include_router(employees_router)
app.include_router(transactions_router)

@app.get("/")
async def root():
    return {"message": "Banking API is running"}
