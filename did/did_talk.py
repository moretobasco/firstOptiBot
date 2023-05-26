from environs import Env
import requests

env = Env()
env.read_env()

did_token = env('DID_TOKEN')

url = "https://api.d-id.com/talks/tlk_QZjx0JjGaPWUdvEgbwuT-"
#
# payload = {
#     "script": {
#         "type": "text",
#         "input": "Moscow is a capital of Russia"
#     },
#     "source_url": "https://create-images-results.d-id.com/DefaultPresenters/Noelle_f/image.jpeg"
# }
headers = {
    "Authorization": "Basic YWxla3NleWxpc2Fuc2tpeUBnbWFpbC5jb20:FO69A9FRp6rHoM6noEmCd",
    "accept": "application/json",
    "content-type": "application/json"
}
#
# response = requests.post(url, json=payload, headers=headers)

id = "tlk_QZjx0JjGaPWUdvEgbwuT-"
response = requests.get(url, headers=headers)
print(response.text)
