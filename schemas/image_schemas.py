from pydantic import BaseModel


class ImageCreate(BaseModel):
    photo_base64: str
