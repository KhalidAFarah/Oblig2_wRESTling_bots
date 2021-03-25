import requests

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

#test code checking if user endpoints functions correctly
#user1 = {"name": "Joe"}
#user2 = {"name": "Moe"}
#print(str(send_POST_Request(base_url + "user", user1)))
#print()
#print(str(send_POST_Request(base_url + "user", user2)))
#print()

#print(str(send_GET_Request(base_url + "users")))

#print(send_DELETE_Request(base_url + "user/2"))

#print(str(send_GET_Request(base_url + "users")))

#testing the room endpoint and checking for errors
print(send_GET_Request(base_url + "rooms"))
print()

print(send_POST_Request(base_url + "room"))
print()
print(send_POST_Request(base_url + "room"))
print()

print(send_GET_Request(base_url + "rooms"))
print()

print(send_GET_Request(base_url + "room/2"))
print()