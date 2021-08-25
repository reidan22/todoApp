from flask import render_template, url_for, request, redirect, Blueprint, flash
from flask_login import login_user, current_user, logout_user, login_required
from todoApp import db
from todoApp.models import User, ToDo
from todoApp.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from todoApp.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__,url_prefix='/user')

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
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
            return "E-mail doesnt exist"
        if user.check_password(form.password.data) and user is not None: 
            login_user(user)
            flash("Log in Success") 

            next = request.args.get('next')

            if next == None or not next[0] == '/' : 
                next = url_for("users.account",id=current_user.id)
            return redirect(next)
        else:
            return "wrong password"

    return render_template('login.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users.route('/tasks')
@login_required
def tasks():
    return render_template('tasks.html')

@users.route('/<int:id>')
@login_required
def account(id):
    return render_template('account.html')

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
        return render_template('account.html')
        return redirect(url_for("users.account",id = current_user.id))
    elif request.method == 'GET' : 
        form.fname.data = current_user.fname
        form.lname.data = current_user.lname
        form.email.data = current_user.email
    profile_image = url_for('static',filename='/resources/img/'+current_user.profile_image)
    return render_template('update.html', profile_image=profile_image,form=form)

@users.route('/<int:id>/delete',methods=["GET",'POST'])
@login_required
def delete(id) : 
    user = User.query.get_or_404(id)
    if user.id != current_user.id  : 
        abort(403)
    # logout_user()
    current_user.delete()
    # db.session.delete(id)
    # db.session.commit()
    flash("User Account Deleted")
    return redirect(url_for("users.login"))
