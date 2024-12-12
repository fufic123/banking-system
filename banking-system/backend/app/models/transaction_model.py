from pydantic import BaseModel, UUID4, Field, root_validator
from typing import Optional, Literal
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: str
    account_id: str
    amount: float
    transaction_type: str
    performed_at: datetime
    performed_via: str
    atm_id: Optional[str]
    branch_id: Optional[str]
    destination_account_id: Optional[str]

class TransactionCreate(BaseModel):
    account_id: UUID4
    amount: float = Field(gt=0)
    transaction_type: Literal['deposit', 'withdrawal', 'transfer']
    performed_via: Literal['atm', 'branch']
    atm_id: Optional[UUID4] = None
    branch_id: Optional[UUID4] = None
    destination_account_id: Optional[UUID4] = None

    @root_validator
    def check_transfer(cls, values):
        ttype = values.get('transaction_type')
        dest_acc = values.get('destination_account_id')
        if ttype == 'transfer' and dest_acc is None:
            raise ValueError("destination_account_id is required for transfers")
        return values

class TransactionUpdate(TransactionCreate):
    # Reuses the same logic as TransactionCreate
    pass
