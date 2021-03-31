import requests
import socket


Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Socket.connect(('localhost', 4242))
base_url = "http://127.0.0.1:5000/api/"

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

