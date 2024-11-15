from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db, init_db
from models import QueryRequest
from schemas import QueryRequestData
from sqlalchemy.future import select
import random
import time
import asyncio

app = FastAPI()


# Инициализация базы данных
@app.on_event("startup")
async def on_startup():
    await init_db()


# Эндпоинт для проверки, что сервер работает
@app.get("/ping")
async def ping():
    return {"message": "Server is running"}


# Эндпоинт для создания запроса
@app.post("/query")
async def create_query(data: QueryRequestData, db: AsyncSession = Depends(get_db)):
    # Создаём новый объект запроса
    new_query = QueryRequest(
        cadastral_number=data.cadastral_number,
        latitude=data.latitude,
        longitude=data.longitude
    )

    try:
        db.add(new_query)
        await db.commit()
        await db.refresh(new_query)
        return {"message": "Query successfully saved", "id": new_query.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


# Эндпоинт для получения истории запросов
@app.get("/history")
async def get_history(cadastral_number: str = None, db: AsyncSession = Depends(get_db)):
    if cadastral_number:
        query = await db.execute(select(QueryRequest).where(QueryRequest.cadastral_number == cadastral_number))
    else:
        query = await db.execute(select(QueryRequest))

    results = query.scalars().all()
    return results


# Эндпоинт /result - эмулирует ответ от внешнего сервера (true/false)
@app.get("/result")
async def get_result():
    # Эмуляция задержки, как если бы запрос обрабатывался долго (до 60 секунд)
    await asyncio.sleep(random.randint(1, 60))  # Симуляция долгой обработки
    return {"result": random.choice([True, False])}  # Возвращает случайное значение true/false
