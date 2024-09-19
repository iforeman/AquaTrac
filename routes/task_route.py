
from flask import Blueprint, render_template, request, redirect, url_for
from models.task import Task
from init_db import session  # Assuming session is set up in init_db.py

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def list_tasks():
    tasks = session.query(Task).all()
    return render_template('task_view.html', tasks=tasks)

@task_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        description = request.form['description']
        due_date = request.form['due_date']
        completed = request.form.get('completed') == 'on'
        type = request.form['type']
        interval = request.form['interval']
        week_day = request.form['week_day']
        new_task = Task(aquarium_id=aquarium_id, description=description, due_date=due_date,
                        completed=completed, type=type, interval=interval, week_day=week_day)
        session.add(new_task)
        session.commit()
        return redirect(url_for('task.list_tasks'))
    return render_template('add_task.html')

@task_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = session.query(Task).get(id)
    if request.method == 'POST':
        task.aquarium_id = request.form['aquarium_id']
        task.description = request.form['description']
        task.due_date = request.form['due_date']
        task.completed = request.form.get('completed') == 'on'
        task.type = request.form['type']
        task.interval = request.form['interval']
        task.week_day = request.form['week_day']
        session.commit()
        return redirect(url_for('task.list_tasks'))
    return render_template('edit_task.html', task=task)

@task_bp.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = session.query(Task).get(id)
    session.delete(task)
    session.commit()
    return redirect(url_for('task.list_tasks'))
