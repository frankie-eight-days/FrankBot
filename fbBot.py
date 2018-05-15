from fbchat import Client
from fbchat.models import *
from chatterbot import ChatBot

chatbot = ChatBot(
    'gf',
    trainer='chatterbot.trainers.ListTrainer'
)

def getResponse(input):
    return(chatbot.get_response(input))

# Subclass fbchat.Client and override required methods
class FrankBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        print(message_object.text)

        if "@Frank Bot" in message_object.text:
            input = message_object.text.replace('@Frank Bot', '')
            print("I was summoned")
            response = getResponse(input)
            if author_id != self.uid:
                self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)
        else:
            print("nobody wants me")


client = FrankBot("frankkevinwalsh@gmail.com", "XXXXXXX")
client.listen()