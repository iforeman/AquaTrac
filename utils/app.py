
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
import logging

# Initialize the Flask application
app = Flask(__name__)

# Load configuration
app.config.from_object('config.DevelopmentConfig')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model
from models.user import User  # Import User model from the models directory

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints with the new naming convention
from routes.aquarium_route import aquarium_bp
app.register_blueprint(aquarium_bp, url_prefix='/aquariums')

# Home route
@app.route('/')
def home():
    return render_template('index.html', message="Welcome to AquaTrac!")

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
