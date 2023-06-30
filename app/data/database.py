import motor.motor_asyncio
from app.config.settings import settings

mongo_database = settings.MONGODB_DATABASE

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
database = client.mongo_database
employee_collection = database.get_collection(settings.MONGODB_COLLECTION)