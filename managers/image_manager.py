from sqlalchemy.ext.asyncio import AsyncSession

from models.image_models import ImageModel, TempImageModel
from schemas.image_schemas import TempImage


class ImageManager:
    @staticmethod
    async def insert_temp_image(file_name: str, db: AsyncSession) -> TempImage:
        image = TempImageModel(file_name=file_name)
        db.add(image)
        await db.commit()
        return TempImage.model_validate(image)
    