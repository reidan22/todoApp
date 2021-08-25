from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from todoApp.models import User

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Log in")

class RegistrationForm(FlaskForm):
    fname = StringField("First Name",validators=[DataRequired()])
    lname = StringField("Last Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(), EqualTo("password_confirm", message = "Password must match")])
    password_confirm = PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been registered already!")
    
class UpdateUserForm(FlaskForm) : 
    fname = StringField("First Name",validators=[DataRequired()])
    lname = StringField("Last Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    picture = FileField("Update Picture", validators =[FileAllowed(["jpg","png"])])

    submit = SubmitField("Update")

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first() : 
            raise ValidationError("Your email has been registered already!")
            
class DeleteUserForm(FlaskForm) : 

    password = PasswordField("Password",validators=[DataRequired(), EqualTo("password_confirm", message = "Password must match")])
    password_confirm = PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField("Delete")

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first() : 
            raise ValidationError("Your email has been registered already!")
