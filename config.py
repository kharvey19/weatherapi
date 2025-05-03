import os
from dotenv import load_dotenv

# loads environment variables from .env to the system's environment
load_dotenv()

VISUAL_CROSSING_API_KEY = os.getenv("VISUAL_CROSSING_API_KEY")
REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
CACHE_TTL = int(os.getenv("CACHE_TTL", 3600))