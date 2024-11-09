#import wave, struct, os
from openai import OpenAI

# client = OpenAI(
#     api_key="sk-oDj6r8Ox2aQCQfBmxPh2IQ", # set this!!!
#     base_url="https://nova-litellm-proxy.onrender.com" # and this!!!
# )
class Chatbot:
    def __init__(self, options):
        self.client = OpenAI(
            api_key="sk-oDj6r8Ox2aQCQfBmxPh2IQ",
            base_url="https://nova-litellm-proxy.onrender.com"
        )
        dietary_restrictions = ""
        for i in options: 
            dietary_restrictions += i + ", "

        content = "You are an assistant, to help people find options for their dietary restrictions. Give all resopnses in concise bullet point form. In the next few prompts, I will provide a zipcode or a restaurant menu. Give food or restaurant options strictly from the menu to consider the following combination of dietary restrictions: " + dietary_restrictions

        self.context = [
            {"role": "system", "content": content},
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
        for message in self.cur_message:
            if message["role"] == "user":
                print(f'USER: {message["content"]}')
            elif message["role"] == "assistant":
                print(f'BOT: {message["content"]}')
    
    def get_bot_response(self):
        return self.cur_message[1]["content"]
    
    def print_chat(self):
        for message in self.context:
            if message["role"] == "user":
                print(f'USER: {message["content"]}')
            elif message["role"] == "assistant":
                print(f'BOT: {message["content"]}')


# options = ["vegetarian", "gluten free"]

# chatbot = Chatbot(options)

# client_input = input()

# while(client_input != "quit"):
#     chatbot.chat(client_input)
#     chatbot.print_cur_message()
#     client_input = input()
#     # print(client_input)

# print("exited loop")