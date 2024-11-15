from pydantic import BaseModel


# Схема данных, которые будут приходить в запросе
class QueryRequestData(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float
