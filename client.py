import requests
import socket
import random
import json
import time


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


base_url = "http://127.0.0.1:5000"
botname = ""
botID = -1

bots=["Jarvis","Stark","Parker","Prime"]

greetings_list=["hi","hello","hey"]
Activities=["read","run","Train","work"]
exit_list=["exit","see you later","bye","quit"]



rooms={}

# Lets the bot get notified when they should get all mesages from a room 
# Note: turning this off means the bot will attempt to fetch message each 30 seconds
push_notification = True

def findaction(message):
    index = 0
    find_greetings = True
    find_activities = True
    find_exits = True

    plausible = {
        "has_greetings": False,
        "activity": "",  
        "has_farewells": False,
    }  # found words from Activities, greetings_list and exit_list resets each round of dialog
    #allow one action per message but can have a greeting and a farewell

    while find_greetings or find_activities or find_exits:
        # looking in the greetings_list if a word is in the message
        if index < len(greetings_list) and greetings_list[index] in message:
            #plausible['gretting']=greetings_list[index])
            plausible['has_greetings'] = True
        else:
            find_greetings = False
        
        # looking in the list of Activities if a word is in the message
        if index < len(Activities) and Activities[index] in message:
            plausible['activity'] = Activities[index]
        else:
            find_activities = False

        # looking in the exit_list if a word is in the message
        if index < len(exit_list) and exit_list[index] in message:
            #plausible.append(exit_list[index])
            plausible['has_farewells'] = True
        else:
            find_exits = False

        index += 1
    return plausible #returns an object of found actions, greeting and/or farewells

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
    #print(str(response))
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

def print_new_messages(messages, room_id):
    #new_messages = False
    counter = 0
    for message_id in messages.keys():
        counter += 1
        if counter > rooms[room_id]['messages_gotten']:
            print(str(messages[message_id])) #printing new messages
            #rooms[room_id]['last_message'] = messages[message_id]['message']
            if messages[message_id]['username'] not in bots:
                #bot responds to messages from non bots
                plausible = findaction(messages[message_id]['message'])
                if botname == bots[0]:# Jarvis
                    send_message(Jarvis(plausible), room_id)
                if botname == bots[1]:# Stark
                    send_message(Stark(plausible), room_id)
                if botname == bots[2]:# Parker
                    send_message(Parker(plausible), room_id)
                if botname == bots[3]:# Prime
                    send_message(Prime(plausible), room_id)

        #if rooms[room_id]['last_message'] == "":
        #    new_messages=True
        #    print(str(messages[message_id])) #printing new messages
        #    rooms[room_id]['last_message'] = messages[message_id]['message']
        #    if messages[message_id]['username'] not in bots:
        #        pass #bot responds to message

        #elif new_messages == False and messages[message_id]['message'] == rooms[room_id]['last_message']:
        #    new_messages = True
            
        #elif new_messages == True:
        #    print(str(messages[message_id])) #printing new messages
        #    rooms[room_id]['last_message'] = messages[message_id]['message']
        #    if messages[message_id]['username'] not in bots:
        #        pass #bot responds to message
        
    rooms[room_id]['messages_gotten'] = counter

def start_up():
    # Registering a new client
    global botname, botID
    print("available bots: ", end="")
    print(*bots, sep=", ")
    while botname not in bots:
        botname = input("choose a bot: ")
    
    user = {"name": botname}
    response = send_POST_Request(base_url + "/api/user", user)
    #print(str(response))
    botID = response['user_id']

    socket.connect(("localhost", 4242))
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
    #print(str(response))
    for room_id in response.keys():

        if push_notification == True:#random.randint(1,5) < 4 and push_notification: # 1/5 chance of not joining the room
            join_a_room(room_id, botID)
            chatroom = {
                #"last_user_message": "",
                #"room_id": room['room_id']
                "messages_gotten": 0
            }
            rooms[int(room_id)] = chatroom
            print(str(rooms))
        elif push_notification == False:# If push notification is off the bot will always join
        
            join_a_room(room_id, botID)
            
            chatroom = {
                #"last_user_message": "",
                #"room_id": room['room_id']
                "messages_gotten": 0
            }
            rooms[int(room_id)] = chatroom

    run()

    

def run():                  # Push notification
    global botname, botID   # It will always be an endpoint to a given room
    while True:             # For example /api/room/1/messages
        if push_notification:
            room_id = int(socket.recv(1024).decode())
            endpoint = base_url + "/api/room/{}/messages".format(room_id)
            response = send_GET_Request(endpoint, {"user_id": botID})
            print_new_messages(response, room_id)
        else:
            time.sleep(30)
            for room_id in rooms.keys():
                endpoint = "/api/room/{}/messages".format(int(room_id))
                response = send_GET_Request(endpoint, {"user_id": botID})
                if len(response.keys()) > rooms[room_id]['messages_gotten']:
                    print_new_messages(response, room_id)

start_up()


            





