from flask import render_template, url_for, request, redirect, Blueprint, flash, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from todoApp import db
from todoApp.models import User, ToDo
from todoApp.users.forms import LoginForm, RegistrationForm, UpdateUserForm, DeleteUserForm
from todoApp.todos.forms import TaskForm
from todoApp.users.picture_handler import add_profile_pic
from datetime import datetime


users = Blueprint('users',__name__,url_prefix='/user')

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit() :
        user = User.query.filter_by(email=form.email.data).first()
        if user: 
            return render_template('err_message.html',err = "E-mail already registered!")
        user = User(fname=form.fname.data,
                    lname=form.lname.data, 
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thank you for registering!")
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None  : 
            return render_template('err_message.html',err = "E-mail doesn't exist")
        if user.check_password(form.password.data) and user is not None: 
            login_user(user)
            flash("Log in Success") 

            next = request.args.get('next')

            if next == None or not next[0] == '/' : 
                next = url_for("users.account",id=current_user.id)
            return redirect(next)
        else:
            return render_template('err_message.html',err = "Wrong Password.")
    return render_template('login.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))

# @users.route('/tasks')
# @login_required
# def tasks():
#     return render_template('tasks.html')

@users.route('/<int:id>/account', methods=['GET','POST'])
@login_required
def account(id):
    form = TaskForm()
    # print("HELLO 1")
    if form.validate_on_submit():
        # print("HELLO 2")
        # if form.done_task.data  : 
        #     return "DONE"
        # elif form.delete_task.data  : 
        #     return "DELEEEETE"
        return redirect(url_for("todos.delete_task"),form =form, id = id)
    page = request.args.get("page",1,type=int)
    user = User.query.filter_by(id=id).first_or_404()
    tasks = ToDo.query.filter_by(author = user).order_by(ToDo.date_target.asc()).paginate(page = page, per_page = 6)
    return render_template('user_tasks.html', tasks = tasks, user = user, time_now = datetime.now(), form = form)

@users.route('/<int:id>/update', methods=['GET','POST'])
@login_required
def update(id):
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data : 
            email = current_user.email
            pic = add_profile_pic(form.picture.data,email)
            current_user.profile_image = pic
        current_user.fname = form.fname.data
        current_user.lname = form.lname.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User Account Updated")
        return redirect(url_for("users.account",id = current_user.id))
    elif request.method == 'GET' : 
        form.fname.data = current_user.fname
        form.lname.data = current_user.lname
        form.email.data = current_user.email
    profile_image = url_for('static',filename='/resources/img/'+current_user.profile_image)
    page = request.args.get("page",1,type=int)
    user = User.query.filter_by(id=id).first_or_404()
    tasks = ToDo.query.filter_by(author = user).order_by(ToDo.date_target.asc()).paginate(page = page, per_page = 6)
    return render_template('update.html', profile_image=profile_image,tasks = tasks, user = user, time_now = datetime.now(),form=form)

@users.route('/<int:id>/delete',methods=["GET",'POST'])
@login_required
def delete(id) :
    form = DeleteUserForm()
    page = request.args.get("page",1,type=int)
    user = User.query.get_or_404(id)
    tasks = ToDo.query.filter_by(author = user).all()
    
    if form.validate_on_submit():
        if user.id != current_user.id  : 
            abort(403)
        if user.check_password(form.password.data) and user.check_password(form.password_confirm.data) and user is not None: 
            db.session.delete(user)
            for task in tasks: 
                db.session.delete(task)
            db.session.commit()
            flash("User Account Deleted")
            return redirect(url_for("users.login"))
        else:
            return render_template('err_message.html',err = "Can't delete. Wrong password.")

    elif form.password.data != form.password_confirm.data : 
            return render_template('err_message.html',err = "Can't delete. Mismatched password")


    tasks = ToDo.query.filter_by(author = user).order_by(ToDo.date_target.asc()).paginate(page = page, per_page = 6)
    return render_template("delete.html",form=form, tasks=tasks, time_now = datetime.now())


@users.route('/err')
def error_message():
    return render_template('err_message.html')

# @users.route('/learn/<int:id>', methods=['GET','POST'])
# def learn(id):
#     user = User.query.filter_by(id=id).first()
#     if user:
#         return jsonify({"id":user.id,"fname":user.fname})
#     return {"id": "None"}, 404