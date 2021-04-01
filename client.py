import requests
import socket
user=input('Choose an User')

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect(('localhost', 4242))
base_url = "http://127.0.0.1:5000/api/"
botID = -1

Bot=["Jarvis","Stark","Parker","Prime"]

greetings_list=["hi","hello","hey"]
Activities=["read","run","Train","work"]
exit_list=["exit","see you later","bye","quit"]

def Jarvis(action):
    if action in greetings_list:
        return"{} Hey Boss!"
    elif action in Activities:
        return "{} sound like a great idea Boss!".format(action+"ing")
    elif action in exit_list:
        return "{} see you soon Boss"
    else:
        return "i didnt understand what you meant"

def Stark(action):
    if action in greetings_list:
        return"{} Howdy partner!"
    elif action in Activities:
        return"{} im lazy to ".format(action)
    elif action in exit_list:
        return "{} chat with you later"
    else:
        return "what do you mean?"

def Prime(action):
    if action in greetings_list:
        return"{}  Hello mate!"
    elif action in Activities:
        return"{} im bussy right now maybe later"
    elif action in exit_list:
        return "{} see you soon"
    else:
        return "what?"

def Parker(action):
    if action in greetings_list:
        return"{}  Hi!"
    elif action in Activities:
        return"{} Not interested"
    elif action in exit_list:
        return "{} bye"
    else:
        return "..."

def receive();
    while True:
        message = client.recv(1024).decode('utf-8')
        if message =="user?":
            client.send(user.encode('utf-8'))
        
        else:
            if ":" in message:
                
                hilsen = message.split(":")
                if hilsen[0] not in 






def send_GET_Request(URI):
    response = requests.get(URI)
    return response.json()
    
def send_POST_Request(URI, data=None):
    response = requests.post(URI, data)
    return response.json()


def send_DELETE_Request(URI, data=None):
    response = requests.delete(URI)
    return response.json()

def send_PUT_Request(URI, data=None):
    response = requests.put(URI, data)
    return response.json()

#message parameter should be a string not an object
def send_message(message, room_id):
    send_POST_Request(base_url+ "room/{}/{}/messages".format(room_id, botID), {"message": message})

def get_all_messages(room_id):
    return send_GET_Request(base_url+ "room/{}/messages".format(room_id), {"user_id": 1})

def create_room():
    send_POST_Request(base_url + "room")

def get_all_rooms():
    return send_GET_Request(base_url + "rooms")
