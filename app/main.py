# Ricardo Amoedo
# version: 1.0

# bibliotecas
from email import contentmanager, message
from turtle import title
from typing import Optional
from urllib import response
from fastapi import Body, FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# instanciando o fastapi
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None


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



# rota raiz
@app.get("/")
def root():
    return {"status": 200, "Message": "ok"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data":post_dict}


@app.get("/posts/{id}")
def get_post(id: int):

    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post com id {id} não encontrado")

    return {"data": post}



@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

    post_dic = post.dict()
    post_dic['id'] = id
    my_posts[index] = post_dic

    return {"data": post_dic}