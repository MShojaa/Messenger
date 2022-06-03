from User_Login import clear, LocalAddress, ServerAddress, DataAddress
from time import sleep
from json import loads

clear()

while True:
    try:
        user_local_file = open(LocalAddress)
        User_Local = loads(user_local_file.read())
        DataServer = ServerAddress + DataAddress
        break
    except:
        pass
    sleep(1)

n = 0
while True:
    try:
        message_file = open(DataServer)
        i = 0
        for line in message_file:
            if i == n:
                message = loads(line)
                if message["username"] == User_Local["username"]:
                    print(f'({message["time"]}) You: {message["text"]}')
                else:
                    print(f'({message["time"]}) {message["username"]}: {message["text"]}')
                n += 1
            i += 1
        message_file.close()
    except:
        pass
    sleep(1)