from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
rooms = {}
users = {}

counter_users = 0
counter_rooms = 0

#user endpoints
def abort_if_user_not_exist(user_id):# in case a the delete request attempts to delete a empty index
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

    def post(self, user_id=None):#auto increments id 
        global counter_users
        counter_users += 1     
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        
        data = parser.parse_args()
        
        #is id needed?
        self.id = counter_users
        self.name = data['name']
        users[counter_users] = self.__dict__

        
        
        return self.__dict__
    
    def delete(self, user_id):
        abort_if_user_not_exist(user_id)
        users.pop(user_id)
        return 200

#endpoint for a specific user for post without userid needed
class UserP(Resource):
    def post(self):#auto increments id 
        global counter_users
        counter_users += 1     

        parser = reqparse.RequestParser()
        parser.add_argument("name")
        data = parser.parse_args()
        
        self.id = counter_users
        self.name = data['name']
        users[counter_users] = self.__dict__
        
        return self.__dict__


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
        return rooms
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
            "id": counter_rooms,
            "users": {},
            "messages": {}
        }

        rooms[counter_rooms] = room
        return room
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
        parser.add_argument("id")
        data = parser.parse_args()

        try:#in case an integer was not passed
            #check if user is registered
            abort_if_user_not_exist(int(data['id']))
        except:
            abort(404, message="not a valid user id given")

        #adding the user to the room
        rooms[room_id]['users'][len(rooms[room_id]['users'])]=users[int(data['id'])]

        return rooms[room_id]['users'][len(rooms[room_id]['users'])-1]
api.add_resource(Room_UsersP, "/api/room/<int:room_id>/user")

#getting all the messages in a room
class Room_messages(Resource):
    def get(self, room_id):

        parser = reqparse.RequestParser()
        parser.add_argument("user_id")
        data = parser.parse_args()
        
        for user in rooms[room_id]['users']:
            if user['id'] == user:
                return rooms[room_id]['messages']

        abort(404, message="the user is not a registered user in the room")
api.add_resource(Room_UsersP, "/api/room/<int:room_id>/messages")




if __name__ == "__main__":
    app.run(debug=True)


