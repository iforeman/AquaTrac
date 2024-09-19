
from flask import Blueprint, render_template, request, redirect, url_for
from models.resource import Resource
from init_db import session  # Assuming session is set up in init_db.py

resource_bp = Blueprint('resource', __name__)

@resource_bp.route('/')
def list_resources():
    resources = session.query(Resource).all()
    return render_template('resource_view.html', resources=resources)

@resource_bp.route('/add', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        title = request.form['title']
        name = request.form['name']
        type = request.form['type']
        quantity = request.form['quantity']
        unit_price = request.form['unit_price']
        total_price = request.form['total_price']
        supplier_id = request.form['supplier_id']
        aquarium_id = request.form['aquarium_id']
        content = request.form['content']
        new_resource = Resource(title=title, name=name, type=type, quantity=quantity,
                                unit_price=unit_price, total_price=total_price,
                                supplier_id=supplier_id, aquarium_id=aquarium_id, content=content)
        session.add(new_resource)
        session.commit()
        return redirect(url_for('resource.list_resources'))
    return render_template('add_resource.html')

@resource_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_resource(id):
    resource = session.query(Resource).get(id)
    if request.method == 'POST':
        resource.title = request.form['title']
        resource.name = request.form['name']
        resource.type = request.form['type']
        resource.quantity = request.form['quantity']
        resource.unit_price = request.form['unit_price']
        resource.total_price = request.form['total_price']
        resource.supplier_id = request.form['supplier_id']
        resource.aquarium_id = request.form['aquarium_id']
        resource.content = request.form['content']
        session.commit()
        return redirect(url_for('resource.list_resources'))
    return render_template('edit_resource.html', resource=resource)

@resource_bp.route('/delete/<int:id>', methods=['POST'])
def delete_resource(id):
    resource = session.query(Resource).get(id)
    session.delete(resource)
    session.commit()
    return redirect(url_for('resource.list_resources'))
