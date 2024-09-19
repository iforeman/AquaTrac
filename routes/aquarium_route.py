
from flask import Blueprint, render_template, request, redirect, url_for
from models.aquarium import Aquarium
from init_db import session  # Assuming session is set up in init_db.py

aquarium_bp = Blueprint('aquarium', __name__)

@aquarium_bp.route('/')
def list_aquariums():
    aquariums = session.query(Aquarium).all()
    return render_template('aquarium_view.html', aquariums=aquariums)

@aquarium_bp.route('/add', methods=['GET', 'POST'])
def add_aquarium():
    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        tank_type = request.form['tank_type']
        shape = request.form['shape']
        capacity = request.form['capacity']
        new_aquarium = Aquarium(name=name, model=model, tank_type=tank_type, shape=shape, capacity=capacity)
        session.add(new_aquarium)
        session.commit()
        return redirect(url_for('aquarium.list_aquariums'))
    return render_template('add_aquarium.html')

@aquarium_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_aquarium(id):
    aquarium = session.query(Aquarium).get(id)
    if request.method == 'POST':
        aquarium.name = request.form['name']
        aquarium.model = request.form['model']
        aquarium.tank_type = request.form['tank_type']
        aquarium.shape = request.form['shape']
        aquarium.capacity = request.form['capacity']
        session.commit()
        return redirect(url_for('aquarium.list_aquariums'))
    return render_template('edit_aquarium.html', aquarium=aquarium)

@aquarium_bp.route('/delete/<int:id>', methods=['POST'])
def delete_aquarium(id):
    aquarium = session.query(Aquarium).get(id)
    session.delete(aquarium)
    session.commit()
    return redirect(url_for('aquarium.list_aquariums'))
