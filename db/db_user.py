from sqlalchemy.orm.session import Session
from db.models import DbUser
from db.hash import Hash
from schemas import UserBase

def create_user(db: Session,request : UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bycrpt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    return db.query(DbUser).all()

def get_user(id,db:Session):
    # handel exceptions
    return db.query(DbUser).filter(DbUser.id == id).first()

def update_user(id:int , request:UserBase, db:Session):
    # handel exceptions
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username : request.username,
        DbUser.email : request.email,
        DbUser.password : Hash.bycrpt(request.password),
    })
    db.commit()
    return 'ok'

def delete_user(id:int , db:Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    # handel exceptions
    return 'User deleted successfully'