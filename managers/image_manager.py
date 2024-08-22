from sqlalchemy.ext.asyncio import AsyncSession

from models.image_model import ImageModel
from schemas.image_schemas import Image


class ImageManager:
    @staticmethod
    async def insert_image(file_name: str, db: AsyncSession) -> Image:
        image = ImageModel(file_name=file_name)
        db.add(image)
        await db.commit()
        return Image.model_validate(image)
    