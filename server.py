from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource, reqparse, abort
import socket
import threading
import json                

app = Flask(__name__) 
api = Api(app)
rooms = {}
users = {}
clientsockets = {}


counter_users = 0
counter_rooms = 0
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def accept_Sockets():
    serversocket.bind(("127.0.0.1", 4242))
    serversocket.listen(4)
    
    while True:
        print("Waiting")
        clientsocket, addr = serversocket.accept()
        print("A fellow bot joined")   #new connection
        data = clientsocket.recv(1024).decode()
        data = json.loads(data)

        
        clientsockets[data['user_id']] = clientsocket
        
def broadcast(room_id):
    global clientsockets
    for userK in rooms[int(room_id)]['users'].keys():
        if rooms[int(room_id)]['users'][userK]['user_id'] in clientsockets.keys():
            # ; is delimeter in case more than message get received in one recv call
            clientsockets[rooms[int(room_id)]['users'][userK]['user_id']].send("{};".format(room_id).encode()) 
accept_socket_thread = threading.Thread(target=accept_Sockets)

        

#user endpoints
def abort_if_user_not_exist(user_id):
    # in case a the delete request attempts to delete a empty index
    found = False
    for ids in users.keys():
        if user_id == ids:
            found = True
    
    if found == False:
        abort(404, message="the user doesn't currently exist")

#endpoint for getting all users
class Users(Resource):
    def get(self):
        return users
api.add_resource(Users, "/api/users")

#endpoint for a specific user
class User(Resource):
    def get(self, user_id):
        return users[user_id]
    
    def delete(self, user_id):
        abort_if_user_not_exist(user_id)
        users.pop(user_id)
        return 200

#endpoint for a specific user for post without userid needed
class UserP(Resource):
    def post(self):
        #auto increments id 
        global counter_users

        if accept_socket_thread.is_alive() == False:
            #a delayed start for the accept_sockets thread
            accept_socket_thread.start()
             

        parser = reqparse.RequestParser()
        parser.add_argument("name")
        data = parser.parse_args()
        
        self.user_id = counter_users
        self.name = data['name']
        
        users[counter_users] = self.__dict__
        counter_users += 1

        response = jsonify(self.__dict__)
        response.headers.add("Access-Control-Allow-Origin", "*")
        
        return response


api.add_resource(User, "/api/user/<int:user_id>")#user id should not be needed 
api.add_resource(UserP, "/api/user")



#endpoints for chat rooms
def abort_if_room_not_exist(room_id):
    found = False
    for room in rooms.keys():
        if room_id == room:
            found = True
    if found == False:
        abort(404, message="Room does not exist")

#get all chat rooms
class Rooms(Resource):
    def get(self):
        data = jsonify(rooms)
        data.headers.add("Access-Control-Allow-Origin", "*")
        return data
api.add_resource(Rooms, "/api/rooms")

#get a chatroom
class Room(Resource):
    def get(self, room_id):
        abort_if_room_not_exist(room_id)
        return rooms[room_id]
api.add_resource(Room, "/api/room/<int:room_id>")

#post a chatroom without a given room_id
class RoomP(Resource):
    def post(self, ):
        global counter_rooms
        counter_rooms += 1

        #making a room dictionary
        room = {
            "room_id": counter_rooms,
            "users": {},
            "messages": {}
        }

        rooms[counter_rooms] = room
        response = jsonify(room)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
api.add_resource(RoomP, "/api/room")

#get all users in the room
class Room_Users(Resource):
    def get(self, room_id):
        return rooms[room_id]['users']
api.add_resource(Room_Users, "/api/room/<int:room_id>/users")

#add a user in the room
class Room_UsersP(Resource):
    def post(self, room_id):
    
        #require a user id in the header?
        parser = reqparse.RequestParser()
        parser.add_argument("user_id")
        data = parser.parse_args()

        try:#in case an integer was not passed
            #check if user is registered
            abort_if_user_not_exist(int(data['user_id']))
        except:
            abort(404, message="not a valid user id given")

        #adding the user to the room
        rooms[room_id]['users'][len(rooms[room_id]['users'])]=users[int(data['user_id'])]

        return rooms[room_id]['users'][len(rooms[room_id]['users'])-1]
api.add_resource(Room_UsersP, "/api/room/<int:room_id>/user")

#getting all the messages in a room
class Room_messages(Resource):
    def get(self, room_id):

        parser = reqparse.RequestParser()
        parser.add_argument("user_id")
        data = parser.parse_args()

        abort_if_room_not_exist(room_id)
        
        for user_id in rooms[room_id]['users'].keys():
            if int(rooms[room_id]['users'][user_id]['user_id']) == int(data['user_id']):
                response = jsonify(rooms[room_id]['messages'])
                response.headers.add("Access-Control-Allow-Origin", "*")
                return response

        abort(404, message="the user is not a registered user in the room")
api.add_resource(Room_messages, "/api/room/<int:room_id>/messages")

#get all of a specific users message or add a user message
class Room_messages_specified(Resource):
    def get(self, room_id, user_id):

        parser = reqparse.RequestParser()
        parser.add_argument("user_id")
        data = parser.parse_args()
        
        for user in rooms[room_id]['users']:
            if int(user) == int(data['user_id']):
                return rooms[room_id]['messages']

        abort(404, message="the user is not a registered user in the room")
    
    def post(self, room_id, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("message")
        data = parser.parse_args()

        message = {
            "user_id": user_id,
            "username": users[int(user_id)]['name'],
            "message": data['message']
        }

        rooms[int(room_id)]['messages'][len(rooms[int(room_id)]['messages'])] = message

        #should broadcast to users with push notifications
        broadcast(room_id)
        return 200


api.add_resource(Room_messages_specified, "/api/room/<int:room_id>/<int:user_id>/messages")

@app.route("/")
def start_a_new_user():
    return render_template('index.html')

@app.route("/<userid>/<name>/")
def select_a_room(userid, name):
    return render_template("rooms.html")

@app.route("/<userid>/<name>/<roomid>")
def start_chatbox(userid, name, roomid):
    return render_template("chatbots.html")

if __name__ == "__main__":   
    app.run(debug=True)


