from pydantic import BaseModel, Field, EmailStr, ConfigDict

from utils.enums import UserRole, AuthProvider


class UserBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=150)
    last_name: str = Field(..., min_length=2, max_length=150)
    email: EmailStr = Field(..., max_length=255)
    phone_number: str = Field(..., min_length=3, max_length=100)


class UserRoleAuth(BaseModel):
    role: UserRole = UserRole.user
    auth_provider: AuthProvider = AuthProvider.internal


class UserPassword(BaseModel):
    password: str = Field(..., min_length=6, max_length=255)


class UserCreate(UserBase, UserPassword, UserRoleAuth):
    pass 


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
