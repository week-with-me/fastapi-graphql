import enum

from pydantic import EmailStr
from sqlalchemy import Column, Enum, String

from src.database import Base


class QNACategory(str, enum.Enum):
    ESTIMATION = '견적문의'
    AS = 'AS문의'
    ETC = '기타문의'


class QNA(Base):
    category: QNACategory = Column('category', Enum(QNACategory), nullable=False)
    title: str = Column('title', String(length=64), nullable=False)
    content: str = Column('content', String(length=1024), nullable=False)
    company: str = Column('company', String(length=32), nullable=False)
    name: str = Column('name', String(length=8), nullable=False)
    phone: str = Column('phone', String(length=8), nullable=False)
    email: EmailStr = Column('email', String(length=32), nullable=False)
    