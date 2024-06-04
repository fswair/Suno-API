import json
import os
import aiohttp

from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

COMMON_HEADERS = {
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer": "https://suno.com",
    "Origin": "https://suno.com",
}

class Suno:
    def __init__(self, token: str = None):
        self.token = token
    @staticmethod
    async def fetch(url: str, headers: dict = None, data: dict = None, method: str = "POST"):
        if headers is None:
            headers = {}
        headers.update(COMMON_HEADERS)
        if data is not None:
            data = json.dumps(data)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    method=method, url=url, data=data, headers=headers
                ) as resp:
                    return await resp.json()
            except Exception as e:
                return f"An error occurred: {e}"

    async def get_feed(self, ids: str):
        headers = {"Authorization": f"Bearer {self.token}"}
        api_url = f"{BASE_URL}/api/feed/?ids={ids}"
        response = await self.fetch(api_url, headers, method="GET")
        return response

    async def generate_music(self, data: dict):
        headers = {"Authorization": f"Bearer {self.token}"}
        api_url = f"{BASE_URL}/api/generate/v2/"
        response = await self.fetch(api_url, headers, data)
        return response

    async def generate_lyrics(self, prompt):
        headers = {"Authorization": f"Bearer {self.token}"}
        api_url = f"{BASE_URL}/api/generate/lyrics/"
        data = {"prompt": prompt}
        return await self.fetch(api_url, headers, data)

    async def get_lyrics(self, lid: str):
        headers = {"Authorization": f"Bearer {self.token}"}
        api_url = f"{BASE_URL}/api/generate/lyrics/{lid}"
        return await self.fetch(api_url, headers, method="GET")

    async def get_credits(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        api_url = f"{BASE_URL}/api/billing/info/"
        response = await self.fetch(api_url, headers, method="GET")
        return {
            "credits_left": response['total_credits_left'],
            "period": response['period'],
            "monthly_limit": response['monthly_limit'],
            "monthly_usage": response['monthly_usage']
        }
