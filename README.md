# Clinic Management Application

This is a **Flask-based web application** designed to manage a clinic's operations, including doctor and patient sign-ups, patient management, and doctor-patient associations. 
The application uses **Flask-WTF** for form handling and **Flask-SQLAlchemy** for database management.

## Features

- **Doctor Management:**
  - Doctor sign-up and sign-in functionalities.
  - View patients assigned to a specific doctor.
  
- **Patient Management:**
  - Patient sign-up by doctors.
  - Search for a specific patient assigned to a doctor.
  
- **Database:**
  - SQLite database integration.
  - Includes models for doctors, patients, and their many-to-many relationships.

## Technologies Used

- Python (Flask)
- Flask-WTF for form handling
- Flask-SQLAlchemy and Flask-Migrate for database management
- SQLite for data storage
- HTML templates with Jinja2 for rendering the frontend

## Installation and Setup

Follow the steps below to set up and run the application:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
Set up a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows

Install Dependencies manually or automatic through requirements.txt :
Flask==2.3.3 ,
Flask-WTF==1.1.1 ,
Flask-SQLAlchemy==3.0.5 ,
Flask-Migrate==4.0.5 ,
Jinja2==3.1.2 ,
WTForms==3.1.0 ,

by:
pip install -r {Dependencies}

or 

pip install -r requirements.txt



For any questions or suggestions, please contact:
Email: ashouryasser11@gmail.com
LinkedIn: https://www.linkedin.com/in/ashour-yasser/


