from motor.motor_asyncio import AsyncIOMotorClient
from sentinel_x.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_client = MongoDB()

async def connect_to_mongo():
    db_client.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db_client.db = db_client.client[settings.DATABASE_NAME]
    
    # High-Scale Indexing: Essential for billions of requests
    # Index by timestamp (DESC) for fast report fetching
    await db_client.db.intelligence.create_index([("timestamp", -1)])
    # Geospatial index for location-based monitoring
    await db_client.db.intelligence.create_index([("location", "2dsphere")])
    # Unique index for users
    await db_client.db.users.create_index("username", unique=True)
    
    print(f"Connected to MongoDB: {settings.DATABASE_NAME} (Indexes ready)")

async def close_mongo_connection():
    db_client.client.close()
    print("Closed MongoDB connection")

# Helper to get the database
def get_database():
    return db_client.db
