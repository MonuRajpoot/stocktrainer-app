#!/usr/bin/env python3
"""
Database initialization script
Run this to set up the database tables
"""

from app import app
from database import db

def init_database():
    """Initialize the database with all tables"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Show existing users
        from database import User
        user_count = User.query.count()
        print(f"Current users in database: {user_count}")
        
        if user_count > 0:
            users = User.query.all()
            for user in users:
                print(f"  - {user.email} ({user.name})")

if __name__ == '__main__':
    init_database()
