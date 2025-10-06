# Interactive Flask App

## Overview
This project is an interactive web application built using Flask, designed to provide users with a variety of educational resources, including courses, quizzes, and a user profile dashboard. The application allows users to sign up, log in, and access personalized content based on their interests.

## Features
- User authentication (signup and login)
- Course listings and details
- Interactive quizzes
- User profile management
- Contact form for inquiries
- Stock market information

## Project Structure
```
interactive-flask-app
├── app.py                  # Main entry point of the application
├── config.py               # Configuration settings for the Flask app
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables
├── templates               # HTML templates for rendering views
│   ├── base.html           # Base template
│   ├── index.html          # Homepage
│   ├── courses.html        # Courses page
│   ├── fundamental.html     # Fundamental topics page
│   ├── basic.html          # Basic topics page
│   ├── technical.html      # Technical subjects page
│   ├── profile.html        # User profile page
│   ├── dashboard.html      # User dashboard
│   ├── contact.html        # Contact page
│   ├── quiz.html           # Quiz interface
│   └── stock_market.html   # Stock market information page
├── static                  # Static files (CSS, JS, images)
│   ├── css
│   │   └── main.css        # Main CSS styles
│   ├── js
│   │   ├── main.js         # Main JavaScript functionality
│   │   ├── auth.js         # Authentication-related JS
│   │   └── quiz.js         # Quiz-related JS
│   └── vendors             # Third-party libraries
├── blueprints              # Modular components of the application
│   ├── auth.py             # Authentication routes and logic
│   ├── courses.py          # Course management routes
│   └── api.py              # API endpoints
├── models                  # Data models
│   └── user.py             # User model
├── forms                   # Form classes
│   └── auth_forms.py       # Authentication forms
├── tests                   # Unit tests
│   └── test_app.py         # Tests for the application
└── README.md               # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd interactive-flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file.

## Usage
1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.