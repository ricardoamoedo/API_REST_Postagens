from pydantic import BaseModel, EmailStr
from datetime import datetime

# schema model
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True



class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    email: EmailStr
    password: str




class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
