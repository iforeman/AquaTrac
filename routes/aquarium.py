# /Users/ian/Documents/Dev/aquatrac/routes/aquarium.py

from flask import Blueprint, render_template

aquarium_bp = Blueprint('aquarium', __name__)

@aquarium_bp.route('/')
def list_aquariums():
    return render_template('aquarium_view.html')
