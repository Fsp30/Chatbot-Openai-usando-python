import openai
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv('API_KEY')
openai.api_key = api_key

# Função para enviar mensagens
def input_message(message, list_messages):
    list_messages.append({
        "role": "user",
        "content": message
    })
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Modelo corrigido
        messages=list_messages
    )
    # Adicionar resposta do chatbot à lista de mensagens
    bot_message = response.choices[0].message  # Atualização para a nova API
    list_messages.append(bot_message)
    return bot_message

# Lista para armazenar mensagens da conversa
list_messages = []

# Loop principal
while True:
    message = input("Your Questions: ")
    if message.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    else:
        response = input_message(message, list_messages)
        print("Chatbot:", response["content"])
