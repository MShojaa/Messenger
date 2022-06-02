from User_Login import Login_To_Account, clear
from json import dump
from time import gmtime

# Check if the user exists or not (for register)
UserName = Login_To_Account()

# Clear the terminal
clear()

user_inputs = {"username": "", "text": "", "time": "", "day": "", "month": "", "year": ""}
while True:
    try:
        # Saving chats
        messege_file = open("./Server/data.json", "a+")

        # Start chatting
        user_inputs["text"] = input(f'{UserName}: ')

        # Chat properties (text, time, ...)
        Chat_Time = gmtime()
        user_inputs["time"] = f'{Chat_Time.tm_hour}:{Chat_Time.tm_min}'
        user_inputs["day"], user_inputs["month"], user_inputs["year"] = Chat_Time.tm_mday, Chat_Time.tm_mon, Chat_Time.tm_year
        user_inputs["username"] = UserName

        # sending messeges to text file
        dump(user_inputs, messege_file)
        messege_file.write('\n')
        messege_file.close()

    except:
        print("Exit!")
        messege_file.close()
        exit()