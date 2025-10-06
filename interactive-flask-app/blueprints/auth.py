from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from forms.auth_forms import LoginForm, SignupForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        password = form.password.data.strip()

        user = USERS.get(email)
        if not user or user.get('password') != password:
            return jsonify({'success': False, 'message': 'Invalid credentials.'}), 401

        session.permanent = True
        session['user_email'] = email
        return jsonify({'success': True})

    return render_template('login.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        email = form.email.data.strip().lower()
        password = form.password.data.strip()

        if email in USERS:
            return jsonify({'success': False, 'message': 'User already exists.'}), 409

        USERS[email] = {
            'name': name,
            'password': password,
        }

        session.permanent = True
        session['user_email'] = email
        return jsonify({'success': True})

    return render_template('signup.html', form=form)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_email', None)
    return jsonify({'success': True})