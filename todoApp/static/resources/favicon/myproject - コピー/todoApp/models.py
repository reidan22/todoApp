from todoApp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    email = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    profile_image = db.Column(db.String(64),nullable=False,default = "default_pic.png")
    tasks = db.relationship("ToDo",backref="author",lazy=True)

    def __init__(self,fname,lname,email,password) : 
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self,password) : 
        return check_password_hash(self.password_hash,password)

    def delete(self) : 
        db.session.delete(self)
        db.session.commit()
        return "Account deleted."


    def __repr__(self) :
        return f"Name: {self.fname} {self.lname} - {self.email} "

class ToDo(db.Model) : 
    users = db.relationship(User)

    # __tablename__ ="todos"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    date_target = db.Column(db.DateTime,nullable=False)
    task_title = db.Column(db.String(128),nullable=False)
    task_details = db.Column(db.Text,nullable=False)
    task_status = db.Column(db.String(16),nullable=False)

    def __init__(self,task_title,task_details,date_target,user_id) : 
        self.task_title = task_title
        self.task_details = task_details
        self.date_target = date_target
        self.user_id = user_id
    
    def __repr__(self) : 
        return f"[TASK ID: {self.id} {self.user_id}]  TITLE:{self.title} STATUS:{self.task_status}"

