from instagrapi import Client
from openai import OpenAI
# from openai import OpenAI
import json

name = 'beauty.json'
output = 'questions.json'

questions = []

#open json file of instagram posts with the hashtag beauty from apify

with open(name, 'r') as file:
    datas = json.load(file)

#print(data[0]['caption'])
    
#create gpt client

client = OpenAI(api_key="Enter your api key")

# function to make chatgpt generate a question based on a prompt

def chat_with_gpt(prompt):
    prefix = 'generate an interesting question based on this caption '
    caption = prefix + prompt
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": caption}])

    return response.choices[0].message.content.strip()

# loop through instagram posts and call chat_with_gpt based on the caption of the post

for data in datas:
    questions.append(chat_with_gpt(data['caption']))

# with open(output, 'w') as json_file:
#     json.dump(questions, json_file)
    
# output result to json file
    
with open(output, 'w') as json_file:
    for question in questions:
        json_file.write(json.dumps(question) + '\n')


