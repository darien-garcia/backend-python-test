import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from alayatodo.db import get_db
from alayatodo.auth import login_required

bp = Blueprint('todos', __name__, url_prefix='/todos')

@bp.route('/home')
@login_required
def home():
    with current_app.open_resource('../README.md', mode='r') as f:
        readme = "".join(l for l in f)
        return render_template('index.html', readme=readme)

@bp.route('/<int:id>/')
@login_required
def todo(id):
    cur = g.db.execute("SELECT * FROM todos WHERE id ='%s'" % id)
    todo = cur.fetchone()
    return render_template('todo/todo.html', todo=todo)


@bp.route('/todo_list')
@login_required
def todo_list():
    print('fetching the todo list for current user')
    cur = g.db.execute("SELECT * FROM todos where user_id='%s'" % session['user_id'])
    todos = cur.fetchall()
    
    return render_template('todo/todos.html', todos=todos)


@bp.route('/new', methods=('GET','POST'))
@login_required
def post():
    g.db.execute(
        "INSERT INTO todos (user_id, description) VALUES ('%s', '%s')"
        % (session['user_id'], request.form.get('description', ''))
    )
    g.db.commit()
    return redirect('/todo')

@bp.route('<int:id>/delete/', methods=('GET', 'DELETE'))
@login_required
def delete(id):
    print("Deleting item id '%s'" % id)
    g.db.execute("DELETE FROM todos where id='%s'" % id)
    g.db.commit()
    return redirect(url_for('todos.todo_list'))