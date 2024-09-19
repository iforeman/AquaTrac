
from flask import Blueprint, render_template, request, redirect, url_for
from models.equipment import Equipment
from init_db import session  # Assuming session is set up in init_db.py

equipment_bp = Blueprint('equipment', __name__)

@equipment_bp.route('/')
def list_equipment():
    equipment_items = session.query(Equipment).all()
    return render_template('equipment_view.html', equipment_items=equipment_items)

@equipment_bp.route('/add', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        type = request.form['type']
        supplier_id = request.form['supplier_id']
        performance_lph = request.form['performance_lph']
        model = request.form['model']
        setup_date = request.form['setup_date']
        purchase_date = request.form['purchase_date']
        unit_price = request.form['unit_price']
        quantity = request.form['quantity']
        total = request.form['total']
        new_equipment = Equipment(aquarium_id=aquarium_id, type=type, supplier_id=supplier_id,
                                   performance_lph=performance_lph, model=model,
                                   setup_date=setup_date, purchase_date=purchase_date,
                                   unit_price=unit_price, quantity=quantity, total=total)
        session.add(new_equipment)
        session.commit()
        return redirect(url_for('equipment.list_equipment'))
    return render_template('add_equipment.html')

@equipment_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_equipment(id):
    equipment = session.query(Equipment).get(id)
    if request.method == 'POST':
        equipment.aquarium_id = request.form['aquarium_id']
        equipment.type = request.form['type']
        equipment.supplier_id = request.form['supplier_id']
        equipment.performance_lph = request.form['performance_lph']
        equipment.model = request.form['model']
        equipment.setup_date = request.form['setup_date']
        equipment.purchase_date = request.form['purchase_date']
        equipment.unit_price = request.form['unit_price']
        equipment.quantity = request.form['quantity']
        equipment.total = request.form['total']
        session.commit()
        return redirect(url_for('equipment.list_equipment'))
    return render_template('edit_equipment.html', equipment=equipment)

@equipment_bp.route('/delete/<int:id>', methods=['POST'])
def delete_equipment(id):
    equipment = session.query(Equipment).get(id)
    session.delete(equipment)
    session.commit()
    return redirect(url_for('equipment.list_equipment'))
