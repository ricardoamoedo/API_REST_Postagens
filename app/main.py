# Ricardo Amoedo
# version: 1.0

# bibliotecas
from email import contentmanager, message
from turtle import title
from typing import Optional, List
from urllib import response
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


# documentação do sqlalchemy
models.Base.metadata.create_all(bind=engine)

# instanciando o fastapi
app = FastAPI()



while True:
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', 
                                user='postgres', password='postgres',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error", error)
        time.sleep(2)


'''
my_posts = [
    {
        "title": "title os post 1", 
        "content": "contente of post 1", 
        "id": 1
    }, {
        "title": "favorite foods", 
        "content": "I like pizza", 
        "id": 2
    }
    ]




def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p



def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

'''





# rota raiz
@app.get("/")
def root():
    return {"status": 200, "Message": "ok"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



