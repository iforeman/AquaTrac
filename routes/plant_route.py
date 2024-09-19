
from flask import Blueprint, render_template, request, redirect, url_for
from models.plant import Plant
from init_db import session  # Assuming session is set up in init_db.py

plant_bp = Blueprint('plant', __name__)

@plant_bp.route('/')
def list_plants():
    plants = session.query(Plant).all()
    return render_template('plant_view.html', plants=plants)

@plant_bp.route('/add', methods=['GET', 'POST'])
def add_plant():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        scientific_name = request.form['scientific_name']
        common_name = request.form['common_name']
        family = request.form['family']
        origin = request.form['origin']
        quantity = request.form['quantity']
        max_size = request.form['max_size']
        height = request.form['height']
        colour = request.form['colour']
        care_level = request.form['care_level']
        lighting = request.form['lighting']
        placement = request.form['placement']
        purchase_date = request.form['purchase_date']
        min_temp = request.form['min_temp']
        max_temp = request.form['max_temp']
        kh_min = request.form['kh_min']
        kh_max = request.form['kh_max']
        ph_min = request.form['ph_min']
        ph_max = request.form['ph_max']
        new_plant = Plant(aquarium_id=aquarium_id, scientific_name=scientific_name, common_name=common_name,
                          family=family, origin=origin, quantity=quantity, max_size=max_size,
                          height=height, colour=colour, care_level=care_level, lighting=lighting,
                          placement=placement, purchase_date=purchase_date, min_temp=min_temp, max_temp=max_temp,
                          kh_min=kh_min, kh_max=kh_max, ph_min=ph_min, ph_max=ph_max)
        session.add(new_plant)
        session.commit()
        return redirect(url_for('plant.list_plants'))
    return render_template('add_plant.html')

@plant_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant(id):
    plant = session.query(Plant).get(id)
    if request.method == 'POST':
        plant.aquarium_id = request.form['aquarium_id']
        plant.scientific_name = request.form['scientific_name']
        plant.common_name = request.form['common_name']
        plant.family = request.form['family']
        plant.origin = request.form['origin']
        plant.quantity = request.form['quantity']
        plant.max_size = request.form['max_size']
        plant.height = request.form['height']
        plant.colour = request.form['colour']
        plant.care_level = request.form['care_level']
        plant.lighting = request.form['lighting']
        plant.placement = request.form['placement']
        plant.purchase_date = request.form['purchase_date']
        plant.min_temp = request.form['min_temp']
        plant.max_temp = request.form['max_temp']
        plant.kh_min = request.form['kh_min']
        plant.kh_max = request.form['kh_max']
        plant.ph_min = request.form['ph_min']
        plant.ph_max = request.form['ph_max']
        session.commit()
        return redirect(url_for('plant.list_plants'))
    return render_template('edit_plant.html', plant=plant)

@plant_bp.route('/delete/<int:id>', methods=['POST'])
def delete_plant(id):
    plant = session.query(Plant).get(id)
    session.delete(plant)
    session.commit()
    return redirect(url_for('plant.list_plants'))
