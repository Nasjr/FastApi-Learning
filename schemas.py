from typing import List
from pydantic import BaseModel


# this will be in the api function
class UserBase(BaseModel):
    username:str
    email:str
    password:str

# article inside user display
class Article(BaseModel):
    title:str
    content:str
    published:bool
    class Config():
        orm_mode = True

class UserDisplay(BaseModel):
    username:str
    email:str
    items : List[Article] = []
    class Config():
        orm_mode = True


# actual article that will be used in requests
class ArticleBase(BaseModel):
    title:str
    content:str
    published:bool
    creator_id: int

# response model

# user inside article display
class User(BaseModel):
    id: int
    username:str
    class Config():
        orm_mode = True

class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user: User
    class Config():
        orm_mode = True