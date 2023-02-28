from send_message_back import send_message, send_picture
from processing_message import process_message
from actors import actor

print('Hello, I am Catfish Chatbot, Whats your name?')
name = input()

print(f"Nice to meet you, {name}!")
print("how are you today?")
user = actor(name)

while True:
    sent_input = input().lower()

    user.ai.clientInput(sent_input)
    user, response = process_message(user, sent_input)
    print(f'Chatbot: {response}')