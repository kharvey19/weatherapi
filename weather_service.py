import httpx
from config import VISUAL_CROSSING_API_KEY

async def fetch_weather(location: str, date: str):

    """
    Sends an async GET request to the Visual Crossing API with 
    the location and date, and returns the weather data in JSON 
    format — or raises an error if something goes wrong.
    """

    # builds the endpoint to get the weather for a given location and date 
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}"
    
    # URL query params to be passed to the API
    params = {
        "key": VISUAL_CROSSING_API_KEY,
        "unitGroup": "metric",
        "include": "days",
        "contentType": "json"
    }

    # create an asynchronous HTTP client session 
    async with httpx.AsyncClient() as client:

        # send a GET request to the specified URL with query parameters
        response = await client.get(url, params=params)

        # rais an error if the respone is not 200 (which means its ok)
        response.raise_for_status()

        # parse and return the response body as a Python dictionary (JSON)
        return response.json()