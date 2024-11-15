from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# URL подключения к базе данных
DATABASE_URL = "postgresql+asyncpg://postgres:8810533@localhost/cadastral_2"

# Создание асинхронного движка и сессии
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Базовый класс для всех моделей
Base = declarative_base()


# Функция для создания сессии базы данных
async def get_db():
    async with SessionLocal() as session:
        yield session


# Инициализация базы данных (создание таблиц)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
