from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database import Base, engine


class ToDo(Base):
    __tablename__ = "ToDo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)