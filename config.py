class Config:
    SECRET_KEY = 'your_secret_key'  # Change this to a random secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/aquatrac.db'  # Main database for development
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True  # Enable debug mode for development

class TestingConfig(Config):
    TESTING = True  # Enable testing mode
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/test_aquatrac.db'  # Separate database for testing

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/prod_aquatrac.db'  # Separate database for production