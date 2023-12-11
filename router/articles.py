from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from auth.oauth2 import get_curr_user, oauth2_scheme
from db import db_article

router = APIRouter(
  prefix='/article',
  tags=['article']
)



# Get all articles
@router.get('/all') #, response_model=ArticleDisplay)
def get_article(db: Session = Depends(get_db)):
  return {
    'data': db_article.get_all_articles(db)
  }
# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), curr_user: UserBase = Depends(get_curr_user)):
  return {
    'data':db_article.create_article(db, request),
    'current_user':curr_user
  }

# Get specific article
@router.get('/{id}') #, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), curr_user: str = Depends(get_curr_user)):
  return {
    'data': db_article.get_article(db, id),
    'current_user':curr_user
  }