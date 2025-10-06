from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME', 'session')
    PERMANENT_SESSION_LIFETIME = 604800  # 7 days in seconds
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///site.db')  # Example for SQLite
    # Add other configuration variables as needed

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}