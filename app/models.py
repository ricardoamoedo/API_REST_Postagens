from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.expression import null
from .database import Base


# Tabela do banco de dados
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=text('now()'))

