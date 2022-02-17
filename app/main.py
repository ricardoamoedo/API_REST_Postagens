# Ricardo Amoedo
# version: 1.0

# bibliotecas
#from email import contentmanager, message
from turtle import title
from typing import Optional
#from urllib import response
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


# documentação do sqlalchemy
models.Base.metadata.create_all(bind=engine)

# instanciando o fastapi
app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True




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



@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data": posts}



@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING 
    #* """, (post.title, post.content, post.publish))
    #new_post = cursor.fetchone()

    #conn.commit()

    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return {"data":new_post}


@app.get("/posts/{id}")
def get_post(id: int,  db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    #post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post com id {id} não encontrado")
    return {"post_detail": post}



@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):

   # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
   # deleted_post = cursor.fetchone()
   # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}")
def update_post(id:int, post: Post):

    cursor.execute("""UPDATE posts SET title = %s,
                    content = %s, published = %s WHERE id = %s
                    RETURNING *""",
                    (post.title, post.content, post.publish, str(id)))
    
    up_post = cursor.fetchone()
    conn.commit()
    
    if up_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

    return {"data": up_post}