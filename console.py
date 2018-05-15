from chatterbot import ChatBot

print("Hello, I am Frank.")

chatbot = ChatBot(
    'gf',
    trainer='chatterbot.trainers.ListTrainer'
)

while(True):
    print("\n")
    text = input()
    response = chatbot.get_response(text)
    print(response)