import requests
import socket

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Socket.connect(('localhost', 4242))

base_url = "http://127.0.0.1:5000/api/"

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

  


