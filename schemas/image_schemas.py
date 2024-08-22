from pydantic import BaseModel, ConfigDict


class ImageBase64(BaseModel):
    photo_base64: str


class TempImage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    file_name: str


class ImageUrl(BaseModel):
    url: str 


class TempImageWithUrl(TempImage, ImageUrl):
    pass
