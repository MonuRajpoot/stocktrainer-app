from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

courses_bp = Blueprint('courses', __name__, template_folder='../templates')

@courses_bp.route('/courses', methods=['GET'])
def courses():
    if 'user_email' not in session:
        return redirect(url_for('base'))
    return render_template('courses.html')

@courses_bp.route('/courses/<course_id>', methods=['GET'])
def course_detail(course_id):
    if 'user_email' not in session:
        return redirect(url_for('base'))
    # Here you would typically fetch course details from a database or data source
    course_info = {
        'id': course_id,
        'title': f'Course {course_id} Title',
        'description': f'Description for course {course_id}.',
        'content': f'Content for course {course_id} goes here.'
    }
    return render_template('course_detail.html', course=course_info)

@courses_bp.route('/api/courses', methods=['GET'])
def api_courses():
    # This would typically fetch courses from a database
    courses_list = [
        {'id': 1, 'title': 'Course 1', 'description': 'Description for Course 1'},
        {'id': 2, 'title': 'Course 2', 'description': 'Description for Course 2'},
        {'id': 3, 'title': 'Course 3', 'description': 'Description for Course 3'},
    ]
    return jsonify(courses_list)

@courses_bp.route('/api/courses/<course_id>', methods=['GET'])
def api_course_detail(course_id):
    # This would typically fetch course details from a database
    course_info = {
        'id': course_id,
        'title': f'Course {course_id} Title',
        'description': f'Description for course {course_id}.',
        'content': f'Content for course {course_id} goes here.'
    }
    return jsonify(course_info)