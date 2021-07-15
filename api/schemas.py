from typing import List, Optional

import graphene
from pydantic import BaseModel


class ItemBase(BaseModel):

    title: str

    description: Optional[str] = None


class ItemCreate(ItemBase):

    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):

    email: str


class UserCreate(UserBase):

    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        # return User.parse_obj(User)
        return "Hello! : " + name


class Mutation(graphene.ObjectType):
    pass
