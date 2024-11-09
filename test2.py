#import wave, struct, os
from openai import OpenAI

client = OpenAI(
    api_key="sk-oDj6r8Ox2aQCQfBmxPh2IQ", # set this!!!
    base_url="https://nova-litellm-proxy.onrender.com" # and this!!!
)
class Chatbot:
    def __init__(self, client):
        self.client = client
        self.context = [
            {"role": "system", "content": "You are an assistant, to help vegetarians find vegetarian options on restaurants' money."},
        ]
        self.total_messages = 0;
        self.cur_message = []

    def chat(self, message):
        self.cur_message = []
        self.context.append(
            {"role": "user", "content": message}
        )
        self.cur_message.append(
            {"role": "user", "content": message}
        )
        response = self.client.chat.completions.create(
            model="gemini/gemini-1.5-pro",
            messages=self.context
        )
        response_content = response.choices[0].message.content
        self.context.append(
            {"role": "assistant", "content": response_content}
        )
        self.cur_message.append(
            {"role": "assistant", "content": response_content}
        )
        self.total_messages += 1

    def print_cur_message(self):
        # print(self.context)
        for message in self.cur_message:
            if message["role"] == "user":
                print(f'USER: {message["content"]}')
            elif message["role"] == "assistant":
                print(f'BOT: {message["content"]}')
    
    def print_chat(self):
        for message in self.context:
            if message["role"] == "user":
                print(f'USER: {message["content"]}')
            elif message["role"] == "assistant":
                print(f'BOT: {message["content"]}')



chatbot = Chatbot(client)

client_input = input()

# while(input != "quit"):
#     chatbot.chat(client_input)
#     chatbot.print_cur_message()
#     client_input = input()