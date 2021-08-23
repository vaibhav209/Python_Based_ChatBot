from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from playsound import playsound
import os
from tkinter import *



Harry = ChatBot("yourbot")

conversation = [
    
    "Hii",
    "Hello, How can I help you?",


    "What’s going on?",
    "Nothing",


    "What is your name?",
    "My name is Harry , I am created by Vaibhav",


    "How are you doing?",
    "I'm doing great",



    "Give me your address?",
    "Sorry I can't",


    "You know Internet?",
    "Its global network of all billions of computers",


    "tell me about cryptocurrency?",
    "A currency which use digital files as money",

    "What is your nick name?",
    "Robot is my nick name",


    "Nice to meet you",
    "Have a goodday :)",


    "Thank you",
    "You're welcome!"
 
]

trainer = ListTrainer(Harry)

#Now training the bot with the help of trainer

trainer.train(conversation)                                    

## For Test a bot in Console ##


# answer = Harry.get_response("Nice to meet you")
# print(answer)

# print("start chat with Michael")

# while True:
#     question = input()
#     if question =='exit':
#         break
#     answer = Harry.get_response(question)
#     print("Harry: ", answer)


#Create a main chatbot window

root = Tk()

root.geometry("400x490")
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)
root.title("Yea.... This is ChatBot !")
root.resizable(0,0)


#Create main logic when user ask question

def ask_Harry():
    quest = txtbox.get("1.0", END)
    answer_Harry = Harry.get_response(quest)
    chatroom.insert(END, "You : " + quest)
    chatroom.insert(END, "Harry : " + str(answer_Harry))
    txtbox.delete(1.0, END)


#Manage all things of Tkinter window (Scrollbar, Background, Button, Key_event, Textbox)


def start_typing(e):
    txtbox.config(background="white", state = NORMAL)
    txtbox.delete(0.0, END)


def mouse_enter(e):
    btn.config(background='#3072ff', foreground = "white")


def mouse_leave(e):
    btn.config(background= 'SystemButtonFace', foreground = 'black')


def send_click(e):
    playsound('send.wav')





scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y)


chatroom = Listbox(root, bg = "#d6d4d4", height = 24, yscrollcommand = scroll.set)
chatroom.pack(fill = BOTH)

scroll.config(command = chatroom.yview)



txtbox = Text(root, bg="white", height=3)


txtbox.insert(0.0, "Type your message")
txtbox.config(state = DISABLED)
txtbox.bind('<Button-1>', start_typing)


txtbox.pack(fill = X)

btn = Button(root, text = "SEND", font = "Helvetica 11", command = ask_Harry)
btn.pack(pady = 8)


btn.bind('<Enter>', mouse_enter)
btn.bind('<Leave>', mouse_leave)
btn.bind('<Button-1>', send_click)



root.mainloop()




