from User_Login import Login_To_Account, clear, ServerAddress, UserAddress, DataAddress
from json import dump
from time import gmtime, sleep

# Check if the user exists or not (for register)
UserName = Login_To_Account(ServerAddress + UserAddress)
sleep(1)

user_inputs = {"username": f'{UserName}', "text": "", "time": "", "day": "", "month": "", "year": ""}
while True:
    try:
        # Clear the terminal
        clear()
        # Start chatting
        user_inputs["text"] = input('You: ')

        # Chat properties (text, time, ...)
        Chat_Time = gmtime()
        minutes = f'0{Chat_Time.tm_min}' if Chat_Time.tm_min < 10 else f'{Chat_Time.tm_min}'
        hours = f'0{Chat_Time.tm_hour}' if Chat_Time.tm_hour < 10 else f'{Chat_Time.tm_hour}'
        user_inputs["time"] = f'{hours}:{minutes}'
        user_inputs["day"], user_inputs["month"], user_inputs["year"] = Chat_Time.tm_mday, Chat_Time.tm_mon, Chat_Time.tm_year

        # sending messages to text file
        message_file = open(ServerAddress + DataAddress, "a+")
        dump(user_inputs, message_file)
        message_file.write('\n')
        message_file.close()

    except:
        print("Exit!")
        message_file.close()
        exit()