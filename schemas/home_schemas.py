from pydantic import BaseModel, Field, ConfigDict


class HomeBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=150)
    city: str = Field(..., min_length=3, max_length=150)
    neighborhood: str = Field(..., min_length=3, max_length=255)
    address: str = Field(..., min_length=3, max_length=255)
    price: int
    year: int


class HomeCreate(HomeBase):
    pass


class Home(HomeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
