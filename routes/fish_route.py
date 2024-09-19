
from flask import Blueprint, render_template, request, redirect, url_for
from models.fish import Fish
from init_db import session  # Assuming session is set up in init_db.py

fish_bp = Blueprint('fish', __name__)

@fish_bp.route('/')
def list_fish():
    fish_list = session.query(Fish).all()
    return render_template('fish_view.html', fish_list=fish_list)

@fish_bp.route('/add', methods=['GET', 'POST'])
def add_fish():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        scientific_name = request.form['scientific_name']
        common_name = request.form['common_name']
        species = request.form['species']
        origin = request.form['origin']
        quantity = request.form['quantity']
        max_size = request.form['max_size']
        min_tank_size = request.form['min_tank_size']
        min_temp = request.form['min_temp']
        max_temp = request.form['max_temp']
        kh_min = request.form['kh_min']
        kh_max = request.form['kh_max']
        ph_min = request.form['ph_min']
        ph_max = request.form['ph_max']
        species_information = request.form['species_information']
        aquarium_care = request.form['aquarium_care']
        feeding_nutrition = request.form['feeding_nutrition']
        diet = request.form['diet']
        aquarium_type = request.form['aquarium_type']
        new_fish = Fish(aquarium_id=aquarium_id, scientific_name=scientific_name, common_name=common_name,
                        species=species, origin=origin, quantity=quantity, max_size=max_size,
                        min_tank_size=min_tank_size, min_temp=min_temp, max_temp=max_temp,
                        kh_min=kh_min, kh_max=kh_max, ph_min=ph_min, ph_max=ph_max,
                        species_information=species_information, aquarium_care=aquarium_care,
                        feeding_nutrition=feeding_nutrition, diet=diet, aquarium_type=aquarium_type)
        session.add(new_fish)
        session.commit()
        return redirect(url_for('fish.list_fish'))
    return render_template('add_fish.html')

@fish_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_fish(id):
    fish = session.query(Fish).get(id)
    if request.method == 'POST':
        fish.aquarium_id = request.form['aquarium_id']
        fish.scientific_name = request.form['scientific_name']
        fish.common_name = request.form['common_name']
        fish.species = request.form['species']
        fish.origin = request.form['origin']
        fish.quantity = request.form['quantity']
        fish.max_size = request.form['max_size']
        fish.min_tank_size = request.form['min_tank_size']
        fish.min_temp = request.form['min_temp']
        fish.max_temp = request.form['max_temp']
        fish.kh_min = request.form['kh_min']
        fish.kh_max = request.form['kh_max']
        fish.ph_min = request.form['ph_min']
        fish.ph_max = request.form['ph_max']
        fish.species_information = request.form['species_information']
        fish.aquarium_care = request.form['aquarium_care']
        fish.feeding_nutrition = request.form['feeding_nutrition']
        fish.diet = request.form['diet']
        fish.aquarium_type = request.form['aquarium_type']
        session.commit()
        return redirect(url_for('fish.list_fish'))
    return render_template('edit_fish.html', fish=fish)

@fish_bp.route('/delete/<int:id>', methods=['POST'])
def delete_fish(id):
    fish = session.query(Fish).get(id)
    session.delete(fish)
    session.commit()
    return redirect(url_for('fish.list_fish'))
