![Weather Image](weather.jpeg)
# Weather API with Redis Caching

This project is a lightweight, backend-only Weather API built using FastAPI. It fetches weather data from the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) and caches responses using Redis for improved performance.

---

## Features

- Fetch current or forecast weather for any location
- Caches responses in Redis to reduce repeated API calls
- Auto-expires cached data after a configurable time
- Built using FastAPI + httpx for async performance
- Clean and simple JSON output

---

## Tech Stack

- **FastAPI** — Web framework
- **httpx** — Async HTTP client
- **Redis** — In-memory cache
- **python-dotenv** — Loads environment config

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/weather-api.git
cd weather-api
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or venv\Scripts\activate on Windows
```

### 3. Install dependencies 
```
pip install -r requirements.txt
```

### 4. Set up your .env file
```
VISUAL_CROSSING_API_KEY=your_api_key
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
CACHE_TTL=3600
```

Get your free API key from [Visual Crossing](https://www.visualcrossing.com/account)

### 5. Start Redis (if not already running)
```
brew install redis          # if Redis isn't installed
brew services start redis   # start Redis as a background service
```
### 6. Run the app
```
uvicorn main:app --reload
```
### 7. Visit in your browser:
```bash
http://localhost:8000/weather?location=New York&date=today
```