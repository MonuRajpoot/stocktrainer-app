from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # In production, hash this!
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

def init_db(app):
    """Initialize database with app context"""
    db.init_app(app)
    
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Migrate existing users from JSON if they exist
        migrate_json_users()

def migrate_json_users():
    """Migrate users from JSON file to database (one-time operation)"""
    import json
    
    users_file = os.path.join(os.path.dirname(__file__), 'users.json')
    
    if os.path.exists(users_file) and User.query.count() == 0:
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                json_users = json.load(f)
            
            for email, user_data in json_users.items():
                existing_user = User.query.filter_by(email=email).first()
                if not existing_user:
                    new_user = User(
                        email=email,
                        name=user_data.get('name', ''),
                        password=user_data.get('password', '')
                    )
                    db.session.add(new_user)
            
            db.session.commit()
            print(f"Migrated {len(json_users)} users from JSON to database")
            
        except Exception as e:
            print(f"Error migrating users: {e}")
            db.session.rollback()
