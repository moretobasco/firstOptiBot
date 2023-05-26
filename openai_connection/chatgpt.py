import openai
from environs import Env

env = Env()
env.read_env()

def chatgpt_response(text):
    openai.api_key = env('OPENAI_TOKEN')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        max_tokens=100
    )
    return response["choices"][0]["text"]

# print(chatgpt_response('Say this is a test'))
