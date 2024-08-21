from sqlalchemy import Column, Integer, String

from db import Base


class HomeModel(Base):
    __tablename__ = "homes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    city = Column(String(150), nullable=False)
    neighborhood = Column(String(255), nullable=False)
    address = Column(String(255))
    price = Column(Integer)
    year = Column(Integer)
