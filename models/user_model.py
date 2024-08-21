from sqlalchemy import Column, Integer, String, Enum

from db import Base
from utils.enums import UserRole, AuthProvider


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(100), nullable=False)
    password = Column(String(255))
    role = Column(Enum(UserRole), nullable=False)
    auth_provider = Column(Enum(AuthProvider), nullable=False)
