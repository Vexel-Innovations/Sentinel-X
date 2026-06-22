from motor.motor_asyncio import AsyncIOMotorClient
from sentinel_x.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_client = MongoDB()

async def connect_to_mongo():
    db_client.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db_client.db = db_client.client[settings.DATABASE_NAME]
    print(f"Connected to MongoDB: {settings.DATABASE_NAME}")

async def close_mongo_connection():
    db_client.client.close()
    print("Closed MongoDB connection")

# Helper to get the database
def get_database():
    return db_client.db
