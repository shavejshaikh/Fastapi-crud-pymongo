import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL : str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_DATABASE : str = os.getenv("MONGODB_DATABASE", "Organisation")
    MONGODB_COLLECTION : str = os.getenv("MONGODB_COLLECTION", "employee")

settings = Settings()