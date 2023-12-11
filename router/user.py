from typing import List
from fastapi import APIRouter, Depends
from auth.oauth2 import get_curr_user
from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user',tags=['user'])

#Create user

@router.post('/',response_model=UserDisplay)
def create_user(reqest:UserBase , db : Session = Depends(get_db)):
    return db_user.create_user(db,reqest)

# Read all users
@router.get('/all',response_model = List[UserDisplay])
def get_all_users(db : Session = Depends(get_db)):
    users =  db_user.get_all_users(db)
    return users

# read user
@router.get('/{id}',response_model = UserDisplay)
def get_user(id: int ,db : Session = Depends(get_db),curr_user: str = Depends(get_curr_user)):
    user =  db_user.get_user(id=id,db=db)
    return user

# Update user
@router.post('/{id}/update')
def update_user(id : int , requset: UserBase, db:Session = Depends(get_db),curr_user: str = Depends(get_curr_user)):
    return db_user.update_user(id,requset,db)


# Delete user
@router.get('/{id}/delete')
def update_user(id : int , db:Session = Depends(get_db),curr_user: str = Depends(get_curr_user)):
    return db_user.delete_user(id,db)
