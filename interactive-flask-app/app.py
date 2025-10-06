from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import timedelta
from blueprints.auth import auth_bp
from blueprints.courses import courses_bp
from blueprints.api import api_bp

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'change-this-secret-in-production'
app.permanent_session_lifetime = timedelta(days=7)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(courses_bp, url_prefix='/courses')
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/', methods=['GET'])
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    return render_template('index.html')

@app.route('/profile')
def profile():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    
    user_email = session['user_email']
    user_info = USERS.get(user_email)
    if not user_info:
        session.pop('user_email', None)
        return redirect(url_for('base'))
    return render_template('profile.html', user=user_info, user_email=user_email)

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    return render_template('dashboard.html')

@app.route('/contact')
def contact():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    return render_template('contact.html')

@app.route('/quiz')
def quiz():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    return render_template('quiz.html')

@app.route('/stock_market')
def stock_market():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    return render_template('stock_market.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_email', None)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)