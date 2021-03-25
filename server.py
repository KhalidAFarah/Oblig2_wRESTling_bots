from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
rooms = {}
users = {}
counter_users = 0

def abort_if_user_not_exist(userid):# in case a the delete request attempts to delete a empty index
    print(users.keys())
    if userid not in  str(users.keys()):
        abort(409, message="the user doesn't currently exist")

#endpoint for getting all users
class Users(Resource):
    def get(self):
        return users
api.add_resource(Users, "/api/users")

#endpoint for a specific user
class User(Resource):
    def get(self, userid):
        return users[userid]

    def post(self, userid):#auto increments id 
        global counter_users
        counter_users += 1     
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        
        data = parser.parse_args()
        
        
        self.id = counter_users
        self.name = data['name']
        users[counter_users] = self.__dict__

        
        
        return self.__dict__
    
    def delete(self, userid):
        abort_if_user_not_exist(userid)
        users.pop(userid)
        return 200

api.add_resource(User, "/api/user/<int:userid>")#user id should not be needed 





class Rooms(Resource):
    pass

if __name__ == "__main__":
    app.run(debug=True)


