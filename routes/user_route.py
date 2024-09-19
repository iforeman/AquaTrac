
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from init_db import session  # Assuming session is set up in init_db.py
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def list_users():
    users = session.query(User).all()
    return render_template('user_view.html', users=users)

@user_bp.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)
        new_user = User(username=username, email=email, password=password, password_hash=password_hash)
        session.add(new_user)
        session.commit()
        return redirect(url_for('user.list_users'))
    return render_template('add_user.html')

@user_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = session.query(User).get(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        password = request.form['password']
        user.password_hash = generate_password_hash(password)
        session.commit()
        return redirect(url_for('user.list_users'))
    return render_template('edit_user.html', user=user)

@user_bp.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user = session.query(User).get(id)
    session.delete(user)
    session.commit()
    return redirect(url_for('user.list_users'))
