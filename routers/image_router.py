from fastapi import APIRouter, Security, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.image_schemas import ImageBase64, TempImageWithUrl
from auth.token import verify_token
from utils.image_compression import compress_image_to_webp
from utils.utils import separate_data_url_from_base64
from image_recognition.google_vision import check_is_safe_and_contains_cat
from storage.google_cloud_storage import upload_bytes_image, async_generate_signed_url
from managers.image_manager import ImageManager
from db import get_db

image_router = APIRouter(prefix="/images", tags=["images"])


@image_router.post(
    "/",
    dependencies=[Security(verify_token)],
    response_model=TempImageWithUrl,
    status_code=status.HTTP_201_CREATED,
)
async def post_image(image_data: ImageBase64, db: AsyncSession = Depends(get_db)):
    base64_data = image_data.photo_base64
    image_bytes = compress_image_to_webp(separate_data_url_from_base64(base64_data)[1])

    if not check_is_safe_and_contains_cat(image_bytes):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Image is not accepted!"
        )

    img_file_name_str = upload_bytes_image(image_bytes)
    image = await ImageManager.insert_temp_image(img_file_name_str, db)
    signed_url = await async_generate_signed_url(img_file_name_str)
    image_with_url = TempImageWithUrl(url=signed_url, **image.model_dump())
    return image_with_url
