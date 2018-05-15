import json
from chatterbot import ChatBot

chatbot = ChatBot(
    'gf',
    trainer='chatterbot.trainers.ListTrainer'
)

frankBot = []

def getMessages(name, fileName):
    with open(fileName, 'r') as dataFile:
        data = json.load(dataFile)

        messageObjects = data['messages']
        cuteMessages = []

        for i in range(len(messageObjects)):
            try:
                if (messageObjects[i]['sender_name'] == name):
                    cuteMessages.append(messageObjects[i]['content'])
                    # print(messageObjects[i]['sender_name'] + ": " + messageObjects[i]['content'])
            except:
                pass
    return cuteMessages

phantomChatList = getMessages('Frank Walsh', 'phantomChat.json')
engineeringChatList = getMessages('Frank Walsh', 'engineeringChat.json')
andrewChatList = getMessages('Frank Walsh', 'andrewChat.json')

print("Phantom Size " + str(len(phantomChatList)))
print("Engineering size: :" + str(len(engineeringChatList)))
print("Andrew size: :" + str(len(andrewChatList)))

chatbot.train(phantomChatList)
chatbot.train(engineeringChatList)
chatbot.train(andrewChatList)