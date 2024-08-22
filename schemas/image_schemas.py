from pydantic import BaseModel, ConfigDict


class ImageCreate(BaseModel):
    photo_base64: str


class Image(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    file_name: str


class ImageUrl(BaseModel):
    url: str 


class ImageWithUrl(Image, ImageUrl):
    pass
