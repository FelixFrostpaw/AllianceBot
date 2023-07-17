import httpx
from urllib.parse import urljoin
import json

GW2_SERVER_URL = "https://api.guildwars2.com/v2/account"
TOKEN_INFO = "tokeninfo"

INVALID_TOKEN_ERROR = '{\n  "text": "Invalid access token"\n}'
UNAUTHORIZED_ERROR = 401


def create_headers(api_key):
  return {"Authorization": f"Bearer {api_key}"}


async def gw2_get_call(api_key, endpoint):
  try:
    async with httpx.AsyncClient() as client:
      headers = create_headers(api_key)
      response = await client.get(endpoint, headers=headers)
      response.raise_for_status()
      parsed_response = json.loads(response.text)
      return {"success": True, "response": parsed_response}
  except httpx.HTTPStatusError as err:
    # Let's specifically catch invalid token errors
    if err.response.status_code == UNAUTHORIZED_ERROR and err.response.text == INVALID_TOKEN_ERROR:
      parsed_response = json.loads(err.response.text)
      return {"success": False, "response": INVALID_TOKEN_ERROR}
    else:
      raise err


async def token_info(api_key):
  endpoint = urljoin(GW2_SERVER_URL, TOKEN_INFO)
  response = await gw2_get_call(api_key, endpoint)
  return response
