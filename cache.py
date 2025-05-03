import redis
import hashlib 
import json
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, CACHE_TTL

# connect to redis 
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

#  create a unique and consistent cache key for each weather request
def generate_cache_key(location: str, date: str) -> str:
    raw_key = f"{location.lower()}_{date}"

    # turn the key into bytes, hash using the SHA-256 algo (256-bit hash value), then converts 
    # the hash from binary to hexidecimal
    return hashlib.sha256(raw_key.encode()).hexdigest()

# looks up the value in Redis for the given cache key
def get_cached_weather(key: str):
    return r.get(key)

# stores the weather data in Redis under the cache key, with a time limit
# seralizes the Python dictionary into a JSON string so Redis can store it simply
def cache_weather_data(key: str, data: dict):
    r.setex(key, CACHE_TTL, json.dumps(data))