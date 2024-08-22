from sqlalchemy import Column, Integer, String, ForeignKey

from db import Base


class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    home_id = Column(Integer, ForeignKey('homes.id'), nullable=False)



class TempImageModel(Base):
    __tablename__ = "temp_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    