from main import Chatbot
class Intermediary():
    def __init__(self):
        self.options = []
        self.chatbot = None
    
    def set_restrictions(self, options):
        self.chatbot = Chatbot(options)
    
    def input_website(self, link):
        self.chatbot.chat(link)
        return self.chatbot.get_bot_response()
    
    def input_zip(self, zipcode, options):
        message = f"Find nearby restaurants in {zipcode} that are guaranteed to have {options} options"
        self.chatbot.chat(message)
        return self.chatbot.get_bot_response()
# test = Intermediary()
# options = ["vegetarian"]
# test.set_restrictions(options)
# web = "https://sammamish.cafesinc.com/Userfiles/Docs/breakfastLunch2024.pdf"
# print(test.input_website(web))