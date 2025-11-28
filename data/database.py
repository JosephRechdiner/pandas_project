from sqlmodel import SQLModel, create_engine, Session
import sqlite3

engine = create_engine("sqlite:///products.db")

def create_db_and_models():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine, expire_on_commit=False) as session:
        yield session