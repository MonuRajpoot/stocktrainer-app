from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import timedelta
import os
from functools import wraps
from database import db, User, init_db

# keep your templates in Project/ (adjust to 'Project/templates' if needed)
app = Flask(__name__, template_folder='Project', static_folder='Project')

# Database configuration
database_url = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Use environment variable for secret key in production
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'change-this-secret-in-production')
app.permanent_session_lifetime = timedelta(days=7)

# Initialize database
init_db(app)

# inject current_user so templates expecting user won't fail
@app.context_processor
def inject_user():
    email = session.get('user_email')
    user = User.query.filter_by(email=email).first() if email else None
    return dict(current_user=user, current_user_email=email)

# small decorator to protect routes
def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if 'user_email' not in session:
            return redirect(url_for('base'))
        return f(*args, **kwargs)
    return wrapped

@app.route('/', methods=['GET'])
def base():
    return render_template('base.html')

@app.route('/home')
@login_required
def home():
    return render_template('index.html')

@app.route('/courses')
@login_required
def courses():
    return render_template('courses.html')

@app.route('/fundamentals')
@login_required
def fundamentals():
    return render_template('fundamental.html')

@app.route('/basics')
@login_required
def basics():
    return render_template('basic.html')

@app.route('/technical')
@login_required
def technical():
    return render_template('technical.html')

@app.route('/profile')
@login_required
def profile():
    email = session.get('user_email')
    user_info = User.query.filter_by(email=email).first()
    if not user_info:
        session.pop('user_email', None)
        return redirect(url_for('base'))
    return render_template('profile.html', user=user_info, user_email=email)

@app.route('/dashboard')
@login_required
def dashboard():
    email = session.get('user_email')
    user_info = User.query.filter_by(email=email).first()
    if not user_info:
        session.pop('user_email', None)
        return redirect(url_for('base'))
    return render_template('dashboard.html', user=user_info, user_email=email)

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')



@app.route('/privacy')
@login_required
def privacy():
    return render_template('privacy.html')



@app.route('/terms')
@login_required
def terms():
    return render_template('terms.html')

@app.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')

@app.route('/stock_market')
@login_required
def stock_market():
    return render_template('stock_market.html')

@app.route('/certificate')
@login_required
def certificate():
    email = session.get('user_email')
    user_info = User.query.filter_by(email=email).first()
    if not user_info:
        session.pop('user_email', None)
        return redirect(url_for('base'))
    
    # Generate certificate data
    from datetime import datetime
    certificate_data = {
        'student_name': user_info.name or 'Student',
        'course_name': 'Advanced Stock Market Fundamentals',
        'completion_date': datetime.now().strftime('%B %d, %Y'),
        'final_score': 95,
        'duration': '8 weeks',
        'grade': 'A+',
        'certificate_id': f"CERT-{datetime.now().year}-SM-{hash(email) % 10000:04d}",
        'instructor': 'Dr. Sarah Chen'
    }
    
    return render_template('certificate.html', **certificate_data)

# logout accepts POST (AJAX) and GET (link)
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_email', None)
    if request.method == 'GET':
        return redirect(url_for('base'))
    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or request.form
    email = (data.get('email') or '').strip().lower()
    password = (data.get('password') or '').strip()

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required.'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or user.password != password:
        return jsonify({'success': False, 'message': 'Invalid credentials.'}), 401

    session.permanent = True
    session['user_email'] = email
    return jsonify({'success': True, 'user': {'email': email, 'name': user.name}})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json(silent=True) or request.form
    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip().lower()
    password = (data.get('password') or '').strip()

    if not name or not email or not password:
        return jsonify({'success': False, 'message': 'Name, email and password are required.'}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'success': False, 'message': 'User already exists.'}), 409

    # Create new user
    new_user = User(email=email, name=name, password=password)  # hash in production
    db.session.add(new_user)
    db.session.commit()

    session.permanent = True
    session['user_email'] = email
    return jsonify({'success': True, 'user': {'email': email, 'name': name}})

# optional: small debug endpoint to confirm template folder
@app.route('/_debug_templates')
def _debug_templates():
    tpl = app.template_folder or ''
    try:
        files = os.listdir(tpl)
    except Exception as e:
        files = [f"error: {e}"]
    return jsonify({'template_folder': tpl, 'exists': os.path.exists(tpl), 'files': files})

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)