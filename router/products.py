import time
from typing import List, Optional
from fastapi import APIRouter, Form, Header, Response, Query
from fastapi.responses import HTMLResponse,PlainTextResponse
from dataclasses import dataclass

router = APIRouter(
    prefix='/proudcts',
    tags=['proudcts']
)




async def time_consuming_func():
    time.sleep(2)

products = ['a','b','c','d','e','f']
@router.get('/all')
async def get_products():
    await time_consuming_func()
    data = ' '.join(products)
    return Response(content=data,media_type='text/plain')

@router.post('/create')
def get_products(name:str = Form(...)):
    products.append(name)
    return products

@router.get('/withheader')
def get_products(custom_header : List[str] = Header(None)):
    return products

@router.get('/{id}', responses = {
    200: {
        "content": {
            'text/html':{
                'example' : '<div>product</div>'
            }
        }
    },
     404: {
        "content": {
            'text/plain':{
                'example' : 'product is not available'
            }
        }
    }
}) 
def get_product(id : int):
    if id > len(products):
        out = 'Product not available'
        return PlainTextResponse(status_code=404,content=out,media_type='text/plain')
    else:
        product = products[id]
        out = f"""
            <head>
            <style>
            .product {{
                width:500px;
                height:30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align : center;
            }}
            </style>
            </head>

            <div class="product"> {product} </div>
            """
        return HTMLResponse(content=out,media_type='text/html')