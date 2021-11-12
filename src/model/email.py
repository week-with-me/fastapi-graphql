import enum

from src.database import Base
from pydantic import EmailStr
from sqlalchemy import Column, String, Enum


class EmailCategory(str, enum.Enum):
    ESTIMATION = '견적문의'
    AS = 'AS문의'
    ETC = '기타문의'


class Email(Base):
    category: EmailCategory = Column('category', Enum(EmailCategory), nullable=False)
    title: str = Column('title', String(length=64), nullable=False)
    content: str = Column('content', String(length=1024), nullable=False)
    compnay: str = Column('company', String(length=32), nullable=False)
    name: str = Column('name', String(length=8), nullable=False)
    phone: str = Column('phone', String(length=8), nullable=False)
    email: EmailStr = Column('email', String(length=32), nullable=False)
    