from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base


@as_declarative()
class Base:
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime = Column(DateTime(timezone=True))
    deleted_at: datetime = Column(DateTime(timezone=True))

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'
