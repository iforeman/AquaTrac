
from flask import Blueprint, render_template, request, redirect, url_for
from models.invertebrate import Invertebrate
from init_db import session  # Assuming session is set up in init_db.py

invertebrate_bp = Blueprint('invertebrate', __name__)

@invertebrate_bp.route('/')
def list_invertebrates():
    invertebrates = session.query(Invertebrate).all()
    return render_template('invertebrate_view.html', invertebrates=invertebrates)

@invertebrate_bp.route('/add', methods=['GET', 'POST'])
def add_invertebrate():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        scientific_name = request.form['scientific_name']
        common_name = request.form['common_name']
        species = request.form['species']
        family = request.form['family']
        sub_family = request.form['sub_family']
        max_size = request.form['max_size']
        min_tank_size = request.form['min_tank_size']
        min_temp = request.form['min_temp']
        max_temp = request.form['max_temp']
        kh_min = request.form['kh_min']
        kh_max = request.form['kh_max']
        ph_min = request.form['ph_min']
        ph_max = request.form['ph_max']
        origin = request.form['origin']
        quantity = request.form['quantity']
        size = request.form['size']
        colour = request.form['colour']
        diet = request.form['diet']
        aquarium_type = request.form['aquarium_type']
        new_invertebrate = Invertebrate(aquarium_id=aquarium_id, scientific_name=scientific_name, common_name=common_name,
                                        species=species, family=family, sub_family=sub_family, max_size=max_size,
                                        min_tank_size=min_tank_size, min_temp=min_temp, max_temp=max_temp,
                                        kh_min=kh_min, kh_max=kh_max, ph_min=ph_min, ph_max=ph_max,
                                        origin=origin, quantity=quantity, size=size, colour=colour,
                                        diet=diet, aquarium_type=aquarium_type)
        session.add(new_invertebrate)
        session.commit()
        return redirect(url_for('invertebrate.list_invertebrates'))
    return render_template('add_invertebrate.html')

@invertebrate_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_invertebrate(id):
    invertebrate = session.query(Invertebrate).get(id)
    if request.method == 'POST':
        invertebrate.aquarium_id = request.form['aquarium_id']
        invertebrate.scientific_name = request.form['scientific_name']
        invertebrate.common_name = request.form['common_name']
        invertebrate.species = request.form['species']
        invertebrate.family = request.form['family']
        invertebrate.sub_family = request.form['sub_family']
        invertebrate.max_size = request.form['max_size']
        invertebrate.min_tank_size = request.form['min_tank_size']
        invertebrate.min_temp = request.form['min_temp']
        invertebrate.max_temp = request.form['max_temp']
        invertebrate.kh_min = request.form['kh_min']
        invertebrate.kh_max = request.form['kh_max']
        invertebrate.ph_min = request.form['ph_min']
        invertebrate.ph_max = request.form['ph_max']
        invertebrate.origin = request.form['origin']
        invertebrate.quantity = request.form['quantity']
        invertebrate.size = request.form['size']
        invertebrate.colour = request.form['colour']
        invertebrate.diet = request.form['diet']
        invertebrate.aquarium_type = request.form['aquarium_type']
        session.commit()
        return redirect(url_for('invertebrate.list_invertebrates'))
    return render_template('edit_invertebrate.html', invertebrate=invertebrate)

@invertebrate_bp.route('/delete/<int:id>', methods=['POST'])
def delete_invertebrate(id):
    invertebrate = session.query(Invertebrate).get(id)
    session.delete(invertebrate)
    session.commit()
    return redirect(url_for('invertebrate.list_invertebrates'))
