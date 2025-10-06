from flask import Flask, session, jsonify
import pytest

# Assuming the app is defined in app.py
from app import app, USERS

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_signup(client):
    response = client.post('/signup', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert response.get_json()['success'] is True

def test_login(client):
    client.post('/signup', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert response.get_json()['success'] is True

def test_logout(client):
    client.post('/signup', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.post('/logout')
    assert response.status_code == 200
    assert response.get_json()['success'] is True

def test_access_protected_route(client):
    response = client.get('/home')
    assert response.status_code == 302  # Should redirect to base if not logged in

    client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.get('/home')
    assert response.status_code == 200  # Should access home if logged in

def test_signup_existing_user(client):
    client.post('/signup', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.post('/signup', json={
        'name': 'Another User',
        'email': 'test@example.com',
        'password': 'newpassword'
    })
    assert response.status_code == 409
    assert response.get_json()['success'] is False

def test_invalid_login(client):
    response = client.post('/login', json={
        'email': 'nonexistent@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.get_json()['success'] is False

def test_profile_access(client):
    response = client.get('/profile')
    assert response.status_code == 302  # Should redirect to base if not logged in

    client.post('/signup', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.get('/profile')
    assert response.status_code == 200  # Should access profile if logged in