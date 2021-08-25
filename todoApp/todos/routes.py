from flask import render_template, url_for, request, redirect, Blueprint, flash
from flask_login import current_user, login_required
from todoApp import db
from todoApp.models import ToDo, User
from todoApp.todos.forms import ToDoForm
from datetime import datetime

todos = Blueprint("todos",__name__,url_prefix='/tasks')

@todos.route('/create',methods=["GET",'POST'])
@login_required
def create_task() : 
    form = ToDoForm()

    if form.validate_on_submit():
        task = ToDo (task_title=form.task_title.data,
                    task_details=form.task_details.data,
                    date_target=form.date_target.data,
                    task_status="OK",
                    user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash("ToDo Task Added!")
        return redirect(url_for("users.account",id=current_user.id))
    page = request.args.get("page",1,type=int)
    tasks = ToDo.query.filter_by(user_id = current_user.id).order_by(ToDo.date_target.asc()).paginate(page = page, per_page = 6)
    return render_template("add_task.html",tasks = tasks, user = current_user, time_now = datetime.now(),form=form)

@todos.route('/<int:todo_id>')
def todo_task(todo_id) : 
    todo = ToDo.query.get_or_404(todo_id)
    return render_template("todo-task.html",task_title=todo.task_title,
                                            task_details=todo.task_details,
                                            date_target = todo.date_target,
                                            user_id = todo.user_id,
                                            task_id = todo.id,
                                            task = todo)

# @todos.route("/<int:id>/list", methods=['GET','POST'])
# @login_required
# def user_tasks(id) :
#     page = request.args.get("page",1,type=int)
#     user = User.query.filter_by(id=id).first_or_404()
#     tasks = ToDo.query.filter_by(author = user).order_by(ToDo.date_target.asc()).paginate(page = page, per_page = 5)
#     return render_template("user_tasks.html", tasks = tasks, user = user)

@todos.route('/<int:task_id>/delete',methods=["GET",'POST'])
@login_required
def delete_task(task_id): 
    task = ToDo.query.get_or_404(task_id)
    id = current_user.id
    if task.author != current_user  : 
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash("Task Deleted")
    return redirect(url_for("users.account",id=id))
    # return redirect(url_for("core.index"))
    # return redirect(url_for("todos.buffer",scroll="account-tasks"))

@todos.route('/buffer')
@login_required
def buffer():
    return render_template("buffer.html")
