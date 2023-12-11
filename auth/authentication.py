from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import models
from db.hash import Hash
from schemas import UserBase
from auth import oauth2

router = APIRouter(tags=['Auth'])


@router.post('/token')
def get_token(request : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user :
        raise HTTPException(status_code=404,detail='invalid credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail='invalid credentials')
    access_token = oauth2.create_access_token(data= {'sub':user.username})
    return {
        'access_token':access_token,
        'type':'bearer',
    }