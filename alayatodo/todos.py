import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, flash
)
from werkzeug.security import check_password_hash, generate_password_hash

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
    cur = g.db.execute("SELECT * FROM todos where user_id='%s'" % session['user_id'])
    todos = cur.fetchall()
    
    return render_template('todo/todos.html', todos=todos)


@bp.route('/new', methods=('GET','POST'))
@login_required
def post():
    error = None
    if not request.form['description']:
        error = 'Description cannot be empty'

    if error == None:

        g.db.execute(
            "INSERT INTO todos (user_id, description) VALUES ('%s', '%s')"
            % (session['user_id'], request.form.get('description', ''))
        )
        g.db.commit()
        flash('Todo item added successfuly')

    if error is not None:
        flash(error)

    return redirect(url_for('todos.todo_list'))

@bp.route('<int:id>/delete/', methods=('GET', 'DELETE'))
@login_required
def delete(id):
    print("Deleting item id '%s'" % id)
    g.db.execute("DELETE FROM todos where id='%s'" % id)
    g.db.commit()
    flash('Item successfully deleted!')
    return redirect(url_for('todos.todo_list'))

@bp.route('<int:id>/json/')
@login_required
def json_item(id):
    todo = get_todo_item(id)
    return render_template('todo/json.html', todo="{ id:'%s', user_id:'%s', desciption:'%s' }" %(todo['id'], todo['user_id'], todo['description']))

def get_todo_item(id):
    todo = cur = g.db.execute("SELECT * FROM todos WHERE id ='%s'" % id)
    todo = cur.fetchone()
    return todo