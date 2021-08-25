from flask import render_template, url_for, request, redirect, Blueprint, flash

core = Blueprint('core',__name__)

todostart_toggle = True

@core.route('/')
def index():
    global todostart_toggle
    if todostart_toggle:
        todostart_toggle = False
        return redirect(url_for('core.todostart'))
    return render_template('index.html')

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/todostart')
def todostart():
    return render_template('todo-start.html')
