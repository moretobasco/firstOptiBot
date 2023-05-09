import requests
import time
from datetime import datetime
from environs import Env

env = Env()
env.read_env()

service_name: str = 'ts1'
opti_token = env('OPTI_TOKEN')


# function for creating url using service name
def _get_url(service_name: str = service_name):
    url = f'https://ws173.optimacros.com/api/v1/service/{service_name}'
    return url

# function for creating cookies using token
def _get_ck(token: str = opti_token) -> dict:
    cookies: dict = {
        'token': token
    }
    return cookies

# function for the first request using url and cookies
# result of the first request is a pair of response token and response id
def _first_request(url=_get_url(), cookies=None):
    if cookies is None:
        cookies = _get_ck()
    response = requests.get(url=url, cookies=cookies)
    response_token = response.json()['params']['responseToken']
    response_id = response.json()['params']['id']
    return response_token, response_id

# function creating modified url and cookies for the second request
# this data uses response token and response id from the first request
def _data_for_second_request(token: str = opti_token):
    response_token, response_id = _first_request()
    modified_cookies: dict = {
        'responseToken': response_token,
        'token': token
    }
    modified_url = f'https://ws173.optimacros.com/api/v1/service/{service_name}/response/{response_id}'
    return modified_cookies, modified_url

# function for the second request
# returns result data from Optimacros
def second_request():
    modified_cookies, modified_url = _data_for_second_request()
    attempt: int = 1
    while True:
        response = requests.get(url=modified_url, cookies=modified_cookies)
        response_status = response.json()['params']['status']
        if response_status == 'IN_PROGRESS':
            print(f'attempt {attempt}')
            print(datetime.now())
            attempt += 1
            time.sleep(2)
            continue
        else:
            # print(response.text)
            break
    return response.json()['params']['data']['result_data']

print(second_request())






