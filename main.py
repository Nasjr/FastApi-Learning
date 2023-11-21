
from fastapi import FastAPI
from router import blog_post
from router import blog_get
#uvicorn main:app --reload
#fastapi-venv\Scripts\activate.bat
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
@app.get('/')
def index():
    return {'message':"Hello world"}



