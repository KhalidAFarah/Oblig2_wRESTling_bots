import requests
import socket
import random
import json


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 4242))

base_url = "http://127.0.0.1:5000"
botname = ""
botID = -1

bots=["Jarvis","Stark","Parker","Prime"]

greetings_list=["hi","hello","hey"]
Activities=["read","run","Train","work"]
exit_list=["exit","see you later","bye","quit"]

rooms={}

# Lets the bot get notified when they should get all mesages from a room 
# Note: turning this off means the bot will attempt to fetch message each minute
push_notification = False

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


def send_GET_Request(URI, data=None):
    response = requests.get(URI,data)
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
    send_POST_Request(base_url+ "/api/room/{}/{}/messages".format(room_id, botID), {"message": message})

def get_all_messages(room_id, ID):
    return send_GET_Request(base_url+ "/api/room/{}/messages".format(room_id), {"user_id": ID})

def create_room():
    return send_POST_Request(base_url + "/api/room")

def get_all_rooms():
    return send_GET_Request(base_url + "/api/rooms")

def join_a_room(room_id, user_id):
    send_POST_Request(base_url+ "/api/room/{}/user".format(room_id), {"user_id": user_id})

def print_new_messages(messages):
    for message_id in messages.keys():
        if

def start_up():
    # Registering a new client
    global botname, botID
    print("available bots: ", end="")
    print(*bots, sep=", ")
    while botname not in bots:
        botname = input("choose a bot: ")
    
    user = {"name": botname}
    response = send_POST_Request(base_url + "/api/user", user)
    botID = response['user_id']

    #sending the user_id over the socket
    #doing this for push notifications
    if push_notification:
        user = {"user_id": botID}
        user = json.dumps(user)
        socket.send(user.encode()) 
    
    # create a room
    create_room()

    #join the created rooms

    response = get_all_rooms()
    for room in response:

        if random.randint(1,5) < 4 and push_notification: # 1/5 chance of not joining the room
            join_a_room(room['room_id'], botID)
        elif push_notification == False:# If push notification is off the bot will always join
        
            join_a_room(room['room_id'], botID)
            room = {
                "last_user_message": "",
            }
            rooms[room['room_id']] = room

    run()

    

def run():                  # Push notification
    global botname, botID   # It will always be an endpoint to a given room
    while True:             # For example /api/room/1/messages
        if push_notification:
            room_id = socket.recv(1024).decode()
            endpoint = "/api/room/{}/messages".format(int(room_id))
            response = send_GET_Request(endpoint, {"user_id": botID})
            print_new_messages(response)

            
        

start_up()


            





