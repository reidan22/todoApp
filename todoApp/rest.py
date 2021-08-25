from todoApp.models import User
from flask_restful import Resource, Api
from todoApp import db, api
from flask import jsonify

class UserREST(Resource) : 
    def get(self,id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.json()
        return {"id": None}, 404

    def delete(self,id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"note": "Delete Success!"}
        return {"id": None}, 404

class UserPost(Resource)  : 

    def post(self,inputString):
        u = inputString.split("&")

        # id = u[0]
        fname = u[0]
        lname = u[1]
        email = u[2]
        password = u[3]

        # user = User.query.filter_by(id=id).first()
        # if not user:
        user = User.query.filter_by(email=email).first()
        if not user  : 
            user = User(
                fname = fname,
                lname = lname,
                email = email,
                password = password
            )
            db.session.add(user)
            db.session.commit()
            return user.json()
        return {"note": "Email already exists"}, 405
        # return {"note": "Id already exists"}, 405

class AllUsers(Resource) : 
    def get(self):
        users = User.query.all()
        return [user.json() for user in users]

class LearnUser(Resource) : 
    def get(self,id):
        user = User.query.filter_by(id=id).first()
        if user:
            return jsonify({"id":user.id,"fname":user.fname})
        return {"id": "None"}, 404



api.add_resource(UserREST,"/rest/<string:id>")
api.add_resource(UserPost,"/rest/post/<string:inputString>")
api.add_resource(AllUsers,"/rest/all")
api.add_resource(LearnUser,"/learn/<string:id>")
