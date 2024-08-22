from sqlalchemy import Column, Integer, String

from db import Base


class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String)
    