import openai
import os
import time

from dotenv import ;pad_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt='你好，'
response=openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=40,
    temperature=0.4,
    stream=True
)

#print(response.choices[0].text)

for chunk in response:
    print(chunk.choices[0].text, end='')
    time.sleep(0.2)