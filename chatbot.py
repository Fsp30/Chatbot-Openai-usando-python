import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
openai.api_key = api_key

def input_message(message, list_messages):
    list_messages.append({
        "role": "user",
        "content": message
    })
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=list_messages
    )
    bot_message = response.choices[0].message
    list_messages.append(bot_message)
    return bot_message
list_messages = []

while True:
    message = input("Your Questions: ")
    if message.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    else:
        response = input_message(message, list_messages)
        print("Chatbot:", response["content"])
