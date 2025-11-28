from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: Optional[int] = Field(foreign_key="owners.id")
    name: str
    price: float
    quantity: int
    category: str
    
    owner: "Owner" = Relationship(back_populates="products")


class Owner(SQLModel, Table=True):
    __tablename__ = "owners"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    products: List["Product"] = Relationship(back_populates="owner")