
from fastapi import FastAPI
from router import user
from router import blog_post
from router import blog_get
from db import models
from db.database import engine
from router import articles
#uvicorn main:app --reload
#fastapi-venv\Scripts\activate.bat
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(articles.router)
@app.get('/')
def index():
    return {'message':"Hello world"}


models.Base.metadata.create_all(engine)



