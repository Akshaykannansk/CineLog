# from fastapi import FastAPI, Query
# from pydantic import BaseModel, AfterValidator
# from typing import Annotated
# import random

# app = FastAPI()

# data = {
#     "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
#     "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
#     "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
# }
# def check_isbn_ids(id: str) -> str:
#     print("Validating ID:", id)
#     if not id.startswith(("isbn-", "imdb-")):
#         raise ValueError("Value of Id is not valid")
#     return id


# @app.get("/items/")
# async def read_items(
#     id: Annotated[str, AfterValidator(check_isbn_ids)],
#     q: Annotated[
#         str | None,
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^[\w]",
#             deprecated=True,
#         ),
#     ] = None,
#     hidden_query: Annotated[
#         str |None, 
#         Query(title="Hidden Query", 
#               alias="hidden-query"
#               ,min_length=5,
#               include_in_schema=False),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     if hidden_query:
#         results.update({"hidden_query":hidden_query})
#     if id:
#        name= data.get(id, "No values Found")
#     else:
#        name = random.choice(list(data.values()))
#     return {'name':name}

# @app.get("/items1/")
# async def read_items1(q: str | None = Query(default= None,min_length=3, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results




from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_session, engine
from app.models import Base, Movie
from app.schemas import MovieCreate, MovieRead
from typing import List

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.post("/movies/", response_model=MovieRead)
def create_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    db_movie = Movie(**movie.dict())
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie

@app.get("/movies/", response_model=List[MovieRead])
def read_movies(session: Session = Depends(get_session)):
    return session.query(Movie).all()