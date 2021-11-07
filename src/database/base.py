from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative
class Base:
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'