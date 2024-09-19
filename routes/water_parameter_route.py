
from flask import Blueprint, render_template, request, redirect, url_for
from models.water_parameter import WaterParameter
from init_db import session  # Assuming session is set up in init_db.py

water_parameter_bp = Blueprint('water_parameter', __name__)

@water_parameter_bp.route('/')
def list_water_parameters():
    water_parameters = session.query(WaterParameter).all()
    return render_template('water_parameter_view.html', water_parameters=water_parameters)

@water_parameter_bp.route('/add', methods=['GET', 'POST'])
def add_water_parameter():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        date = request.form['date']
        temperature_min = request.form['temperature_min']
        temperature_max = request.form['temperature_max']
        ph_min = request.form['ph_min']
        ph_max = request.form['ph_max']
        gh_min = request.form['gh_min']
        gh_max = request.form['gh_max']
        kh_min = request.form['kh_min']
        kh_max = request.form['kh_max']
        nitrite_min = request.form['nitrite_min']
        nitrite_max = request.form['nitrite_max']
        nitrate_min = request.form['nitrate_min']
        nitrate_max = request.form['nitrate_max']
        ammonium_min = request.form['ammonium_min']
        ammonium_max = request.form['ammonium_max']
        copper_min = request.form['copper_min']
        copper_max = request.form['copper_max']
        oxygen_min = request.form['oxygen_min']
        oxygen_max = request.form['oxygen_max']
        conductivity_min = request.form['conductivity_min']
        conductivity_max = request.form['conductivity_max']
        new_water_parameter = WaterParameter(aquarium_id=aquarium_id, date=date, temperature_min=temperature_min,
                                             temperature_max=temperature_max, ph_min=ph_min, ph_max=ph_max,
                                             gh_min=gh_min, gh_max=gh_max, kh_min=kh_min, kh_max=kh_max,
                                             nitrite_min=nitrite_min, nitrite_max=nitrite_max, nitrate_min=nitrate_min,
                                             nitrate_max=nitrate_max, ammonium_min=ammonium_min, ammonium_max=ammonium_max,
                                             copper_min=copper_min, copper_max=copper_max, oxygen_min=oxygen_min,
                                             oxygen_max=oxygen_max, conductivity_min=conductivity_min, conductivity_max=conductivity_max)
        session.add(new_water_parameter)
        session.commit()
        return redirect(url_for('water_parameter.list_water_parameters'))
    return render_template('add_water_parameter.html')

@water_parameter_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_water_parameter(id):
    water_parameter = session.query(WaterParameter).get(id)
    if request.method == 'POST':
        water_parameter.aquarium_id = request.form['aquarium_id']
        water_parameter.date = request.form['date']
        water_parameter.temperature_min = request.form['temperature_min']
        water_parameter.temperature_max = request.form['temperature_max']
        water_parameter.ph_min = request.form['ph_min']
        water_parameter.ph_max = request.form['ph_max']
        water_parameter.gh_min = request.form['gh_min']
        water_parameter.gh_max = request.form['gh_max']
        water_parameter.kh_min = request.form['kh_min']
        water_parameter.kh_max = request.form['kh_max']
        water_parameter.nitrite_min = request.form['nitrite_min']
        water_parameter.nitrite_max = request.form['nitrite_max']
        water_parameter.nitrate_min = request.form['nitrate_min']
        water_parameter.nitrate_max = request.form['nitrate_max']
        water_parameter.ammonium_min = request.form['ammonium_min']
        water_parameter.ammonium_max = request.form['ammonium_max']
        water_parameter.copper_min = request.form['copper_min']
        water_parameter.copper_max = request.form['copper_max']
        water_parameter.oxygen_min = request.form['oxygen_min']
        water_parameter.oxygen_max = request.form['oxygen_max']
        water_parameter.conductivity_min = request.form['conductivity_min']
        water_parameter.conductivity_max = request.form['conductivity_max']
        session.commit()
        return redirect(url_for('water_parameter.list_water_parameters'))
    return render_template('edit_water_parameter.html', water_parameter=water_parameter)

@water_parameter_bp.route('/delete/<int:id>', methods=['POST'])
def delete_water_parameter(id):
    water_parameter = session.query(WaterParameter).get(id)
    session.delete(water_parameter)
    session.commit()
    return redirect(url_for('water_parameter.list_water_parameters'))
