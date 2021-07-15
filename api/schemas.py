from typing import List, Optional

import graphene
from pydantic import BaseModel

import database
import models

# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True

# class UserBase(BaseModel):

#     email: str

# class UserCreate(UserBase):

#     password: str

# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True

db = database.db_session.session_factory()


class PostSchema(BaseModel):
    title: str
    content: str


class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, content):
        post = PostSchema(title=title, content=content)
        db_post = models.Post(title=post.title, content=post.content)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        ok = True
        return CreateNewPost(ok=ok)


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        # return User.parse_obj(User)
        return "Hello! : " + name


class Mutation(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()
