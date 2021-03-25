from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
rooms = {}
users = {}
counter_users = 0

#def abort_if_user_exist(userid):


#endpoint for getting all users
class Users(Resource):
    def get(self):
        return users
api.add_resource(Users, "/api/users")

#endpoint for a specific user
class User(Resource):
    def get(self, userid):
        return users[userid]

    def post(self, name):#auto increments id
        self.name = name
        users[counter_users] = self.__dict__
        counter_users += 1
        return self.__dict__
    
    def delete(self, userid):
        users.pop(userid)
        return 200






class Rooms(Resource):
    pass


