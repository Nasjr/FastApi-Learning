from typing import Optional, List
from fastapi import APIRouter, Query , Body , Path
from pydantic import BaseModel, Field 

router = APIRouter(prefix='/blog',tags=['blog'])
class ImageModel(BaseModel):
    url : str = Field(...,max_length=250)
    alias : str
class BlogModel(BaseModel):
    title:str
    content:str
    published: Optional[bool]
    no_commments: int
    image: Optional[ImageModel] = None

@router.post('/new')
def create_blog(blog : BlogModel):
    return {'data':blog}

@router.post('/new/comment/{id}')
def create_blog(blog : BlogModel, id:int = Path(lt=100), 
                
                 content: str = Body(Ellipsis,min_length=5,
                                     max_length=250,regex='^[a-z\s]*$'),

                version: int=Query(None,alias='commentId',
                                   title='Add a Comment',description='comment id for new comment',deprecated=False),
                v: List[str] = Query(...)
               
                ):
    return {
        'data':blog,
        'comment_id':id,
        'version':version,
        'content':content,
        'v':v
        }