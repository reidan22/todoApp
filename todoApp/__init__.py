import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
## REST API
from flask_restful import Resource, Api




app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

api = Api(app)
db = SQLAlchemy(app)
Migrate(app,db)
CORS(app)
################################################################
##   LOGIN CONFIGS   ###########################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
################################################################
from todoApp.core.routes import core
from todoApp.users.routes import users
from todoApp.todos.routes import todos

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(todos)

from todoApp import rest



# puppies = [
#     {"name":"Dan","color":"RED"}
# ]
# class PuppyPost(Resource):
#     def post(self,inputString):
#             # Add  the dictionary to list
#         pup = inputString.split("&")
#         pup ={
#                 'name':pup[0],
#                 "color":pup[1]
#                 }
#         puppies.append(pup)
#         # Then return it back
#         print(puppies)
#         return pup

# class PuppyNames(Resource):
#     def get(self,name):
#         print(puppies)

#         # Cycle through list for puppies
#         for pup in puppies:
#             if pup['name'] == name:
#                 return pup

#         # If you request a puppy not yet in the puppies list
#         return {'name':None},404

#     def post(self, list):
#         # Add  the dictionary to list
#         pup = [{'name':name}]
#         puppies.append(pup)
#         # Then return it back
#         print(puppies)
#         return pup

#     def delete(self,name):

#         # Cycle through list for puppies
#         for ind,pup in enumerate(puppies):
#             if pup['name'] == name:
#                 # don't really need to save this
#                 delted_pup = puppies.pop(ind)
#                 return {'note':'delete successful'}

        


# class AllNames(Resource):

#     def get(self):
#         # return all the puppies :)
#         return {'puppies': puppies}


# api.add_resource(PuppyNames, '/puppy/<string:name>')
# api.add_resource(PuppyPost, '/puppy/post/<string:inputString>')
# api.add_resource(AllNames,'/puppies')


