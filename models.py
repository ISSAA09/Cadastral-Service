from sqlalchemy import Column, Integer, String, Float
from database import Base


# Модель данных запроса
class QueryRequest(Base):
    __tablename__ = "query_requests"

    id = Column(Integer, primary_key=True, index=True)
    cadastral_number = Column(String(255), index=True, nullable=False)  # Укажите длину для String
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
