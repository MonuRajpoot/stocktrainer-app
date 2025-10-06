from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/api/user', methods=['GET'])
def get_user_info():
    user_email = request.args.get('email')
    if user_email in USERS:
        return jsonify({'success': True, 'user': USERS[user_email]}), 200
    return jsonify({'success': False, 'message': 'User not found.'}), 404

@api.route('/api/courses', methods=['GET'])
def get_courses():
    courses = [
        {'id': 1, 'title': 'Course 1', 'description': 'Description for Course 1'},
        {'id': 2, 'title': 'Course 2', 'description': 'Description for Course 2'},
        {'id': 3, 'title': 'Course 3', 'description': 'Description for Course 3'},
    ]
    return jsonify({'success': True, 'courses': courses}), 200

@api.route('/api/quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    user_email = session.get('user_email')
    if not user_email:
        return jsonify({'success': False, 'message': 'User not logged in.'}), 401

    score = data.get('score')
    # Here you would typically save the score to a database or perform some logic
    return jsonify({'success': True, 'message': 'Quiz submitted successfully.', 'score': score}), 200

@api.route('/api/logout', methods=['POST'])
def api_logout():
    session.pop('user_email', None)
    return jsonify({'success': True, 'message': 'Logged out successfully.'}), 200