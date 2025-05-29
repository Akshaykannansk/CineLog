from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    genre: str
    year: int
    rating: float

class MovieRead(MovieCreate):
    id: int
