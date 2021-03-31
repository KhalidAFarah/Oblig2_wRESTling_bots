import requests
import socket

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Socket.connect(('localhost', 4242))

base_url = "http://127.0.0.1:5000/api/"
botname = "Stark"
botID = -1

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