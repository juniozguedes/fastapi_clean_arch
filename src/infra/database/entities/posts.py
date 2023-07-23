from sqlalchemy import Column, String, Integer
from src.infra.database.settings.base import Base


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
