# from fastapi import FastAPI
# import uvicorn
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name = str
#     price = float
#     # is_offer = bool = None
#
#
# @app.get("/")
# def get_item():
#     return "get data "
#
#
# @app.get("/items/{item_id}")
# def get_items(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/item/{item.id}")
# def put_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def root():
#     return ['item1', 'item2', 'item3', 'item4']
#
#
# @app.post("/todo")
# def create_todo():
#     return "create todo item"
#
#
# @app.get("/todo/{id}")
# def read_todo(id: int):
#     return f"read todo item with id {id}"
#
#
# @app.put("/todo/{id}")
# def update_todo(id: int):
#     return "update todo item with id {id}"
#
#
# @app.delete("/todo/{id}")
# def delete_todo(id: int):
#     return "delete todo item with id {id}"
#
#
# @app.get("/todo")
# def read_todo_list():
#     return "read todo list"

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer

app = FastAPI()

# SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3:'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee = bool
    food = bool

    class Config:
        orm_mode = True


@app.post('/places')
async def create_place(place: Place):
    return place


@app.get('/')
async def get_place():
    return {'message': 'Hello this is a get data'}
