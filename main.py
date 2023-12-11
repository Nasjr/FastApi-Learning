
import asyncio
import time
from fastapi import FastAPI, Request
from fastapi.websockets import WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from exceptions import StroyException
from router import user,blog_get,blog_post, products,articles , files
from fastapi.staticfiles import StaticFiles
from auth import authentication
from db import models
from db.database import engine
from client import html

#fastapi-venv\Scripts\activate.bat
#uvicorn main:app --reload

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(products.router)
app.include_router(articles.router)
app.include_router(authentication.router)
app.include_router(files.router)


@app.get('/hi')
def index():
    return {'message':"Hello world"}

@app.get('/')
async def create_connection():
    return HTMLResponse(html)
clients = []

@app.websocket('/chat')
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)

# handler for exceptions
@app.exception_handler(StroyException)
def story_exception_handler(request : Request,exc:StroyException):
    return JSONResponse(status_code=418,content={'details':exc.name})
# database creation
models.Base.metadata.create_all(engine)

# List of local urls of applications like react
origins_url = ['http://127.0.0.1:8000']

# if you are using ex: react program from the same machine that tries to access your backend
app.add_middleware(CORSMiddleware,
                    allow_origins = origins_url,
                    allow_credentials = True, 
                    allow_methods = ['*'],allow_headers = ['*'])

@app.middleware('http')
async def middle_ware(request:Request,call_next):
    start = time.time()
    response = await call_next(request)
    end = time.time()
    response.headers['duration'] = str(end - start)
    return response

app.mount('/files',StaticFiles(directory='files'),name='files')
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)


