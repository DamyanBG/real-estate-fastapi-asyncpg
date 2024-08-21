from os import environ
from dotenv import load_dotenv

load_dotenv()

JWT_KEY = environ["JWT_KEY"]

SA_KEY_PATH = environ["SA_KEY_PATH"]
BUCKET_NAME = environ["BUCKET_NAME"]

DB_USER = environ["DB_USER"]
DB_PASSWORD = environ["DB_PASSWORD"]
DB_HOST = environ["DB_HOST"]
DB_NAME = environ["DB_NAME"]

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
