from User_Login import *
from time import localtime, strftime, sleep
from os import system, name

def clear():
   # for windows
   if name == 'nt':
        _ = system('cls')
   # for mac and linux
   else:
        _ = system('clear')

sleep(1)
clear()

user_inputs = dict()

def getting_messege(user_inputs):
    try:
        # creating text file where messeges save
        messege_file = open("data.json", "a+")

        # getting messege
        text_input = input("Enter your messege: ")
        user_inputs["text"] = text_input
        # describe the time the messege sent
        user_inputs["time"] = strftime("%H:%M", localtime())
        user_inputs["day"] = strftime("%d", localtime())
        user_inputs["month"] = strftime("%b", localtime())
        user_inputs["year"] = strftime("%Y", localtime())
        # if user wants to leave
        if text_input.lower() == "exit":
            print("you left")
            exit()
        # sending messeges to text file
        dump(user_inputs, messege_file)
        messege_file.write('\n')
        messege_file.close()
        # messege_file.write(str(user_inputs["text"] + "\n"))
        # messege_file.write(str(user_inputs["time"] + "\n"))
        # messege_file.write("\n")
    # if input has error
    except:
        print("Program closed.")
        messege_file.close()
        exit()

while True:
    getting_messege(user_inputs)