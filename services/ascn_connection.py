import aiohttp
import asyncio
from environs import Env
from datetime import datetime


env = Env()
env.read_env()

service_name: str = 'ts1'
opti_token = env('OPTI_TOKEN')



# function for creating url using service name
async def _get_url(service_name: str = service_name):
    url = f'https://ws173.optimacros.com/api/v1/service/{service_name}'
    return url

# function for creating cookies using token
async def _get_ck(token: str = opti_token) -> dict:
    cookies: dict = {
        'token': token
    }
    return cookies


# function for the first request using url and cookies
# result of the first request is a pair of response token and response id
async def _first_request(url=None, cookies=None):
    if url is None:
        url = await _get_url()
    if cookies is None:
        cookies = await _get_ck()
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, cookies=cookies) as response:
            response_json = await response.json()
            response_token = response_json['params']['responseToken']
            response_id = response_json['params']['id']
            return response_token, response_id


# function creating modified url and cookies for the second request
# this data uses response token and response id from the first request
async def _data_for_second_request(token: str = opti_token):
    response_token, response_id = await _first_request()
    modified_cookies: dict = {
        'responseToken': response_token,
        'token': token
    }
    modified_url = f'https://ws173.optimacros.com/api/v1/service/{service_name}/response/{response_id}'
    return modified_cookies, modified_url


# function for the second request
# returns result data from Optimacros
async def second_request():
    modified_cookies, modified_url = await _data_for_second_request()
    attempt: int = 1
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=modified_url, cookies=modified_cookies) as response:
                response_json = await response.json()
                response_status = response_json['params']['status']
                if response_status == 'IN_PROGRESS':
                    print(f'attempt {attempt}')
                    print(datetime.now())
                    attempt += 1
                    await asyncio.sleep(2)
                    continue
                else:
                    # print(response.text)
                    break
    return response_json['params']['data']['result_data']


# loop = asyncio.get_event_loop()
# loop.run_until_complete(second_request())