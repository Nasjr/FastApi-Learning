from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker





SQLALCHEMY_DATABASE_URL = 'sqlite:///E://Courses//Python//Fastapi-Practice//fastapi.db'

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread':False} 
    )

Sessionlocal = sessionmaker(autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()