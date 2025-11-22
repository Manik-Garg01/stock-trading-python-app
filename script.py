import requests
import os
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&apiKey={POLYGON_API_KEY}"
response = requests.get(url)
print(response.json())