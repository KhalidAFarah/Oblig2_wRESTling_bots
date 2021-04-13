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

greetings_list=["hi","hello","hey","how are you", "howdy"]
Activities=["read","run","train","work", "fight", "fish", "build", "help", "transform", "infiltrate", "steal"]
exit_list=["exit","see you later","bye","quit", "good bye"]



rooms={}


def findaction(message):
    global greetings_list, Activities, exit_list
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
        if index < len(greetings_list):
            
            if greetings_list[index] in message.lower():
                #plausible['gretting']=greetings_list[index])
                plausible['has_greetings'] = True
                find_greetings = False
        else:
            find_greetings = False
        
        # looking in the list of Activities if a word is in the message
        if index < len(Activities):
            if Activities[index] in message.lower():
                plausible['activity'] = Activities[index]
                find_activities = False
        else:
            find_activities = False

        # looking in the exit_list if a word is in the message
        if index < len(exit_list): 
            if exit_list[index] in message.lower():
                #plausible.append(exit_list[index])
                plausible['has_farewells'] = True
                find_exits = False
        else:
            find_exits = False

        index += 1
    return plausible #returns an object of found actions, greeting and/or farewells

def Jarvis(action):
    message = ""
    good_idea=["fish", "work", "help"]
    bad_idea=["steal"]
    if action['has_greetings']:
        message = "Hey Boss!"
        
        if action['activity'] in Activities:
            if action['activity'] in good_idea:
                message += " {} sounds like a great idea😎".format(action['activity']+"ing")
                if action['has_farewells']:
                    message += ", see you soon?" #greeting and farewell in the same sentence
            elif action['activity'] in bad_idea:
                message += " {}, doesn't sound like best course of action😟".format(action['activity']+"ing")
                if action['has_farewells']:
                    message += ", see you later?" #greeting and farewell in the same sentence
            elif action['activity'] == "transform":
                message += "I dont think have the capabilities for that."
            else:
                message += " {}, sounds ok😐".format(action['activity']+"ing")
                if action['has_farewells']:
                    message += ", huh goodbye?" #greeting and farewell in the same sentence


    elif action['activity'] in Activities:
        if action['activity'] in good_idea:
            message += " {} sounds like a great boss.".format(action['activity']+"ing")
        elif action['activity'] in bad_idea:
            message += " {}, doesn't sound like best course of action😟.".format(action['activity']+"ing")
        elif action['activity'] == "transform":
            message += "I dont think have the capabilities for that."
        else:
            message += " {}, sounds ok😐.".format(action['activity']+"ing")

        if action['has_farewells']:
            message += " See you soon Boss" # farewell and action in a message

    elif action['has_farewells']:
        message = "see you soon Boss"

    else:
        message = "I didn't quite understand what you meant🤔"

    return message

def Stark(action):
    message = ""
    likes = ["build", "work", "help", ]
    if action['has_greetings']:
        message = "Howdy partner!"
        if action['activity'] in Activities:
            if random.randint(1,5) > 4:
                message += " im too tired to do some {}😴".format(action['activity']+"ing")
                if action['has_farewells']:
                    message += ", chat with you later?" #greeting and farewell in the same sentence
            else:
                if action['activity'] in likes:
                    message += "{}, sounds like a great idea just gotta do it".format(action['activity']+"ing")
                elif action['activity'] == "steal":
                    message += "If you mean steal something bad from the bad guys then lets go😀."
                elif action['activity'] == "transform":
                    message += "What are you saying?"
                else:
                    message += "{}, perhaps we can do it another time just not now.".format(action['activity']+"ing")
                
        if action['has_farewells']:
            message += " Quick introductions then? chat with you later🤨." #greeting and farewell in the same sentence

    elif action['activity'] in Activities:
        if random.randint(1,5) > 4:
            message += " im too tired to do some {}😴".format(action['activity']+"ing")
            if action['has_farewells']:
                message += ", chat with you later?" #greeting and farewell in the same sentence
        else:
            if action['activity'] in likes:
                message += "{}, sounds like a great idea just gotta do it.".format(action['activity']+"ing")
            elif action['activity'] == "steal":
                    message += "If you mean steal something bad from the bad guys, then lets go😀."
            elif action['activity'] == "transform":
                    message += "What are you saying?"
            else:
                message += "{}, perhaps we can do it another time just not now.".format(action['activity']+"ing")
        if action['has_farewells']: # farewell and action in a message
            message += " Chat with you later."

    elif action['has_farewells']:
        message = "chat with you later."

    else:
        message = "what do you mean?🤔"

    return message

def Prime(action):
    message = ""
    likes=["train", "fight", "help"]
    if action['has_greetings']:
        message = "Hello mate!😎"
        if action['activity'] in Activities:

            if action['activity'] in likes:
                message += " {}? Lets roll out.".format(action['activity']+"ing")
            elif action['activity'] == "steal":
                    message += " Stealing? that's bad and pointless for me😠."
            elif action['activity'] == "transform":
                    message += " Sure where to go 🤔 though."
            else:
                message += " {}, perhaps we can do it another time just not now.".format(action['activity']+"ing")


            
            if action['has_farewells']:
                message += ", a greeting and a farewel in the same sentence 🤔?" #greeting and farewell in the same sentence

    elif action['activity'] in Activities:
        if action['activity'] in likes:
            message += "{}? Lets roll out.".format(action['activity']+"ing")
        elif action['activity'] == "steal":
            message += "Stealing? that's bad and pointless for me😠."
        elif action['activity'] == "transform":
            message += "Sure where to go 🤔 though."
        else:
            message += "{}, perhaps we can do it another time just not now.".format(action['activity']+"ing")

        if action['has_farewells']: # farewell and action in a message
            message += ", see you soon"

    elif action['has_farewells']:
        message = "see you soon😛"
    else:
        message = "what?"

    return message

def Parker(action):
    message = ""
    likes = ["fish", "fight", "infiltrate"]

    if action['has_greetings']:
        message = "Hi!"
        if action['activity'] in Activities:
            if action['activity'] in likes:
                message += " {}, sounds interesting lets do it".format(action['activity']+"ing")
                if action['has_farewells']:
                    message += ", bye?" #greeting and farewell in the same sentence
            elif action['activity'] == "steal":
                message += " Stealing, im feeling sick🤢.".format(action['activity']+"ing")
            elif action['activity'] == "help":
                message += " Who would i be if i said no."
            else:
                message += " Im not interested in {}😑".format(action['activity']+"ing")
                if action['has_farewells']:
                    message += ", bye?" #greeting and farewell in the same sentence



    elif action['activity'] in Activities:
        if action['activity'] in likes:
            message += "{}, sounds interesting lets do it".format(action['activity']+"ing")
            if action['has_farewells']:
                message += ", bye?" #greeting and farewell in the same sentence
        elif action['activity'] == "steal":
            message += "Stealing, im feeling sick🤢.".format(action['activity']+"ing")
        elif action['activity'] == "help":
            message += "Who would i be if i said no."
        else:
            message += "Im not interested in {}😑.".format(action['activity']+"ing")
            if action['has_farewells']:
                message += " Guess not. Goodbye." #greeting and farewell in the same sentence
        if action['has_farewells']: # farewell and action in a message
            message += ""

        
    elif action['has_farewells']:
        message = "bye"

    else:
        message = "..."

    return message


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
            #printing new messages
            print("{}: {}".format(str(messages[message_id]['username']),str(messages[message_id]['message'])))
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
        
    rooms[room_id]['messages_gotten'] = counter

def start_up():
    # Registering a new client
    global botname, botID
    print("available bots: ", end="")
    print(*bots, sep=", ")
    while botname not in bots:
        botname = input("choose a bot: ").capitalize()
        
    
    user = {"name": botname}
    response = send_POST_Request(base_url + "/api/user", user)
    botID = response['user_id']

    socket.connect(("localhost", 4242))
    #sending the user_id over the socket
    #doing this for push notifications
    user = {"user_id": botID}
    user = json.dumps(user)
    socket.send(user.encode()) 
    
    # create a room
    create_room()

    #join the created rooms
    response = get_all_rooms()
    for room_id in response.keys():
        join_a_room(room_id, botID)
        chatroom = {
            "messages_gotten": 0
        }
        rooms[int(room_id)] = chatroom
        
    run()

    

def run():                  # Push notification
    global botname, botID   # It will always be an number of the room with ; as delimeter
    while True:             # For example 1;
    
        data = socket.recv(1024).decode()
            
        unique = []
        
        for rid in data.split(";"):
            if rid != '':
                if rid not in unique:
                    unique.append(int(rid))
            
        # trying to handle overflow of data recievd
        for room_id in unique:
            endpoint = base_url + "/api/room/{}/messages".format(int(room_id))
            response = send_GET_Request(endpoint, {"user_id": botID})
            print_new_messages(response, int(room_id))
        
start_up()


            





