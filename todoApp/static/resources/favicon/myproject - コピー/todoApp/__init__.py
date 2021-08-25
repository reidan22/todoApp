import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

# api = Api(app)
db = SQLAlchemy(app)
Migrate(app,db)
################################################################
##   LOGIN CONFIGS   ###########################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
################################################################
from todoApp.core.routes import core
from todoApp.users.routes import users
# from puppycompanyblog.error_pages.handlers import error_pages
# from puppycompanyblog.blog_posts.views import blog_posts
app.register_blueprint(core)
app.register_blueprint(users)
# app.register_blueprint(blog_posts)
# app.register_blueprint(error_pages)