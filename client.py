import requests

base_url = "http://127.0.0.1:5000"

def send_GET_Request(URI):
    response = requests.get(URI)
    return response.json()

def send_POST_Request(URI, data):
    response = requests.post(URI, data)
    return response.json()

def send_DELETE_Request(URI, data=None):
    response = requests.delete(URI)
    return response.json()

def send_PUT_Request(URI, data=None):
    response = requests.put(URI, data)
    return response.json()

#test code checking if user endpoints functions correctly
user1 = {"name": "Joe"}
#user2 = {"name": "Moe"}
print(str(send_POST_Request(base_url + "/api/user/", user1)))
#print()
#print(str(send_POST_Request(base_url + "/api/user/0", user2)))
#print()

#print(str(send_GET_Request(base_url + "/api/users")))

#print(send_DELETE_Request(base_url + "/api/user/2"))

#print(str(send_GET_Request(base_url + "/api/users")))