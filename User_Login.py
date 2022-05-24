from json import dump, loads
from os import system, name
from pty import slave_open
from time import sleep

def Register():
    User = {"username": "", "password": ""}
    User["username"] = input("Welcome!\nEnter your username: (Caution: UserName is case sensitive) ")
    User["password"] = input("Enter your password: ")
    user_local_file = open("./User_Local.json", "w")
    user_server_file = open("./Server/User_Server.json", "a+")
    dump(User, user_local_file)
    dump(User, user_server_file)
    user_local_file.close()
    user_server_file.write('\n')
    user_server_file.close()

def Login_To_Account():
    try:
        user_local_file = open("./User_Local.json")
        user_server_file = open("./Server/User_Server.json")

        User_Local = loads(user_local_file.read())
        for line in user_server_file:
            User_Server = loads(line)
            # UserName is case sensitive
            # Check if the username is exsited or not
            if User_Local["username"] == User_Server["username"]:\
                # Greeting to user
                print(f'Hi {User_Local["username"]}')
                while True:
                    password = input("Enter your password: ")
                    if password == User_Server["password"]:
                        print(f'You may now enter to your account {User_Local["username"]}!')
                        break
                    else:
                        print("Wrong password!")
                break
            else:
                Register()

        user_local_file.close()
        user_server_file.close()
    except:
        # If none of the "User_Local.json" or "User_Server.json" exists, the user must register so he/she can enter the App
        Register()
    return User_Local["username"]

def clear():
    # Clear the terminal

    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Mac and Linux
    else:
        _ = system('clear')
    sleep(1)