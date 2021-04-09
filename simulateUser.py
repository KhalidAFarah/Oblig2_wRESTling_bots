import requests
import time
# This skript is meant to quickly set up test and check for error
# Feel free to mess around and change values

print("\U0001F923")

# Reminder remove file before handing in
base_url = "http://127.0.0.1:5000/api/"
read_messages = 0

def send_GET_Request(URI, data=None):
    response = requests.get(URI, data)
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

print("Adding two new users")
user1 = {"name": "Joe"}
response = send_POST_Request(base_url + "user", user1)
id1 = response['user_id']
print(str(response))
print()

print("Adding to room 1")
print(send_POST_Request(base_url+ "room/1/user", {"user_id": id1}))
print()

print("Getting all messages in room 1")
print(send_GET_Request(base_url+ "room/1/messages", {"user_id": id1}))
print()

print("Getting all users in room 1 should include both users")
print(send_GET_Request(base_url+ "room/1/users"))
print()

print("Getting all messages in room 1 should return {}")
print(send_GET_Request(base_url+ "room/1/messages", {"user_id": id1}))
print()

while True:
    time.sleep(5)
    print("Getting all messages in room 1")
    response = send_GET_Request(base_url+ "room/1/messages", {"user_id": id1})
    print(response)
    print()
    

    print("Posting a message to the room")
    message = input("write a message: ")
    print(send_POST_Request(base_url+ "room/1/{}/messages".format(id1), {"message": message}))
    print()