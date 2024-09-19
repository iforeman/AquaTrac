import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
import logging
from config import Config, TestConfig

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app(config_class=Config):
    # Initialize the Flask application
    app = Flask(__name__)

    # Load configuration
    if os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(config_class)

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # User model
    from models.user import User  # Import User model from the models directory

    # User loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints for all routes
    from routes.aquarium_route import aquarium_bp
    from routes.equipment_route import equipment_bp
    from routes.expense_route import expense_bp
    from routes.fish_route import fish_bp
    from routes.income_route import income_bp
    from routes.invertebrate_route import invertebrate_bp
    from routes.plant_route import plant_bp
    from routes.resource_route import resource_bp
    from routes.supplier_route import supplier_bp
    from routes.task_route import task_bp
    from routes.user_route import user_bp
    from routes.water_parameter_route import water_parameter_bp

    app.register_blueprint(aquarium_bp, url_prefix='/aquariums')
    app.register_blueprint(equipment_bp, url_prefix='/equipment')
    app.register_blueprint(expense_bp, url_prefix='/expenses')
    app.register_blueprint(fish_bp, url_prefix='/fish')
    app.register_blueprint(income_bp, url_prefix='/incomes')
    app.register_blueprint(invertebrate_bp, url_prefix='/invertebrates')
    app.register_blueprint(plant_bp, url_prefix='/plants')
    app.register_blueprint(resource_bp, url_prefix='/resources')
    app.register_blueprint(supplier_bp, url_prefix='/suppliers')
    app.register_blueprint(task_bp, url_prefix='/tasks')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(water_parameter_bp, url_prefix='/water_parameters')

    # Home route
    @app.route('/')
    def home():
        return render_template('index.html', message="Welcome to AquaTrac!")

    # Error handling
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
