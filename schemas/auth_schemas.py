from pydantic import BaseModel, EmailStr, Field


class TokenResp(BaseModel):
    access_token: str
    token_type: str = "bearer"


class CredentialsReq(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=255)
