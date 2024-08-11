import re

class SimpleChatBot:
    def __init__(self):
        self.responses = {
            r"my name is (.*)": ["Hello %1, How are you today?"],
            r"hi|hey|hello": ["Hello", "Hey there"],
            r"what is your name ?": ["I am a chatbot created by OpenAI. You can call me ChatGPT."],
            r"how are you ?": ["I'm doing good. How about you?"],
            r"sorry (.*)": ["Its alright", "Its OK, never mind"],
            r"i'm (.*) doing good": ["Nice to hear that", "Alright, great!"],
            r"what (.*) want ?": ["Make me an offer I can't refuse"],
            r"(.*) created ?": ["I was created by OpenAI.", "OpenAI created me."],
            r"(.*) (location|city) ?": ['I am based in the cloud.'],
            r"how is the weather in (.*)?": ["Weather in %1 is always fantastic.", "I am not sure about the weather in %1."],
            r"quit": ["Bye for now. See you soon.", "It was nice talking to you. Bye."],
            r"(.*)": ["That's interesting.", "Tell me more.", "I see.", "Can you elaborate?"]
        }

    def respond(self, message):
        for pattern, responses in self.responses.items():
            match = re.match(pattern, message, re.IGNORECASE)
            if match:
                response = responses[0]
                for i in range(len(match.groups())):
                    response = response.replace(f"%{i+1}", match.group(i+1))
                return response
        return "I don't understand that."

def chatbot():
    print("Hi, I'm the chatbot you built. Start talking to me!")
    bot = SimpleChatBot()
    while True:
        message = input("You: ")
        if message.lower() in ["quit", "exit"]:
            print("Bot: Bye for now. See you soon.")
            break
        response = bot.respond(message)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
