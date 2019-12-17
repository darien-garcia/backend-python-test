import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, flash, abort
)
from werkzeug.security import check_password_hash, generate_password_hash

from alayatodo.auth import login_required
from alayatodo.models import todos as todos_model 
from alayatodo import db

bp = Blueprint('todos', __name__, url_prefix='/todos')
ITEMS_PER_PAGE = 3

@bp.route('/home')
@login_required
def home():
    with current_app.open_resource('../README.md', mode='r') as f:
        readme = "".join(l for l in f)
        return render_template('index.html', readme=readme)

@bp.route('/<int:id>/')
@login_required
def todo(id):
    todo = get_todo_item(id)
    return render_template('todo/todo.html', todo=todo)


@bp.route('/todo_list')
@login_required
def todo_list():
    page = request.args.get('page', 1, type=int)
    query = db.session.query(todos_model).filter(
        todos_model.user_id == session['user_id']
        )
    total = 10
    todos = query.paginate(page, ITEMS_PER_PAGE, False)

    next_url = url_for('todos.todo_list', page=todos.next_num) \
        if todos.has_next else None
    prev_url = url_for('todos.todo_list', page=todos.prev_num) \
        if todos.has_prev else None
    next_num=todos.next_num \
        if todos.has_next else 0
    prev_num=todos.prev_num \
        if todos.has_prev else 0

    return render_template('todo/todos.html', 
                           todos=todos.items,
                           next=next_num,
                           prev=prev_num,
                           page_total = total,
                           next_url=next_url,
                           prev_url=prev_url)


@bp.route('/new', methods=('GET','POST'))
@login_required
def post():
    error = None
    if not request.form['description']:
        error = 'Description cannot be empty'

    if error == None:
        new_todo = todos_model(
            description=request.form.get('description', ''),
            user_id=session['user_id']
            )
        db.session.add(new_todo)
        db.session.flush()
        db.session.commit()
        flash("Todo item << %s >> was successfully inserted" % new_todo.description)
    if error is not None:
        flash(error)

    return redirect(url_for('todos.todo_list'))

@bp.route('<int:id>/delete/', methods=('GET', 'DELETE'))
@login_required
def delete(id):
    todo = get_todo_item(id)
    db.session.query(todos_model).filter(todos_model.id==id).delete()
    db.session.commit()
    flash("Todo item << %s >> was successfully deleted" % todo.description)
    return redirect(url_for('todos.todo_list'))

@bp.route('<int:id>/json/')
@login_required
def json_item(id):
    todo = get_todo_item(id)
    
    if todo is not None:
        if todo.user_id != session['user_id']:
            abort(403)
        return render_template('todo/json.html', todo="{ id:'%s', user_id:'%s', desciption:'%s' }" %(todo.id, todo.user_id, todo.description))
    abort(404)

def get_todo_item(id):
    return db.session.query(todos_model).filter(todos_model.id==id).first()