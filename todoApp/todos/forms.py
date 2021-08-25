from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class ToDoForm(FlaskForm) : 
    task_title = StringField("Task",validators=[DataRequired()])
    task_details = TextAreaField("Details",validators=[DataRequired()])
    date_target = DateField("Target Date",validators=[DataRequired()])
    submit = SubmitField("Add Task")

class TaskForm(FlaskForm) : 

    done_task = SubmitField("Done")
    delete_task = SubmitField("x")