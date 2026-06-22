import redis
import json
from sentinel_x.core.config import settings

# Initialize Redis for caching
# Caching common requests is vital for handling billions of requests
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class CacheService:
    @staticmethod
    def get(key: str):
        data = r.get(key)
        return json.loads(data) if data else None

    @staticmethod
    def set(key: str, value: dict, expire: int = 3600):
        r.setex(key, expire, json.dumps(value))

cache_service = CacheService()
