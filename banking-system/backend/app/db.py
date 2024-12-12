import asyncpg
import os
from fastapi import Depends

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/banking_db")

async def connect_db():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn

async def get_db_connection():
    conn = await connect_db()
    try:
        yield conn
    finally:
        await conn.close()
