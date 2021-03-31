import requests
# This skript is meant to quickly set up test and check for error
# Feel free to mess around and change values

#print("\U0001F923")

# Reminder remove file before handing in
base_url = "http://127.0.0.1:5000/api/"

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

# Testing that the user endpoints are functioning correctly
print("Getting all users should be {} if the server just started")
print(str(send_GET_Request(base_url + "users")))
print()

print("Adding two new users")
user1 = {"name": "Joe"}
user2 = {"name": "Moe"}
print(str(send_POST_Request(base_url + "user", user1)))
print()

print(str(send_POST_Request(base_url + "user", user2)))
print()

print("Getting all users again should include the two posted users")
print(str(send_GET_Request(base_url + "users")))
print()

print("Deleting the second user should retun the status code 200")
print(send_DELETE_Request(base_url + "user/2"))
print()

print("Deleting the second user again should return a message")
print(send_DELETE_Request(base_url + "user/2"))
print()

print("Checking all users once again")
print(str(send_GET_Request(base_url + "users")))
print()


# Testing the room endpoints and checking for errors
print("Getting all the rooms should be {} if the server just started")
print(send_GET_Request(base_url + "rooms"))
print()

print("Creating two new rooms")
print(send_POST_Request(base_url + "room"))
print()
print(send_POST_Request(base_url + "room"))
print()

print("Getting all rooms again")
print(send_GET_Request(base_url + "rooms"))
print()

print("Getting the first room")
print(send_GET_Request(base_url + "room/1"))
print()

print("Getting the second room")
print(send_GET_Request(base_url + "room/2"))
print()

# Testing the room add and get all users endpoints
print("Getting all users in room 1 should be {}")
print(send_GET_Request(base_url+ "room/1/users"))
print()

print("Adding back the sescond user")
print(str(send_POST_Request(base_url + "user", user2)))
print()

print("Adding both users to room 1")
print(send_POST_Request(base_url+ "room/1/user", {"id": 1}))
print()

# Testing if moe can get all messages
print("Getting all messages in room 1 should return an error")
print(send_GET_Request(base_url+ "room/1/messages", {"user_id": 3}))
print()


print(send_POST_Request(base_url+ "room/1/user", {"id": 3}))# Moes id will be 3 assuming the server just started
print()

print("Getting all users in room 1 should include both users")
print(send_GET_Request(base_url+ "room/1/users"))
print()

print("Getting all users in room 2 should be {}")
print(send_GET_Request(base_url+ "room/2/users"))
print()

# Testing if moe now can get all messages
print("Getting all messages in room 1 should return {}")
print(send_GET_Request(base_url+ "room/1/messages", {"user_id": 3}))
print()

print("Posting a message to the room")
print(send_POST_Request(base_url+ "room/1/3/messages", {"message":"helllplp!"}))
print()

print("Getting all messages in room 1 should return moes message")
print(send_GET_Request(base_url+ "room/1/messages", {"user_id": 3}))
print()

print("Posting a message to the room")
print(send_POST_Request(base_url+ "room/1/1/messages", {"message":"no i wont"}))
print()

print("Getting all messages in room 1 should return moe and joes message")
print(send_GET_Request(base_url+ "room/1/messages", {"user_id": 1}))
print()