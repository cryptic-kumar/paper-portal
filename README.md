# Paper Portal

## Description

Paper Portal is a web application built with **Flask** and **Bootstrap** that allows users to submit, manage, and review academic papers. It supports different user roles such as **Publisher**, **Recommender**, and **Admin**, each with distinct functionalities. Publishers can submit papers, Recommenders can review them, and Admins can manage users and papers. The project uses **SQLite** as the database and **Flask-Login** for authentication.

---

## Features

- **User Roles**: Publisher, Recommender, Admin.
- **User Authentication**: Secure login and registration with role-based access.
- **Paper Submission**: Publishers can submit new papers with title, abstract, and file upload.
- **Paper Review**: Recommenders can accept or reject submitted papers.
- **Admin Dashboard**:
  - View all users and papers.
  - Change user roles (Publisher, Recommender, Admin).
  - Delete users or papers.
- **Responsive UI**: Built using **Bootstrap 5**, compatible with mobile and desktop devices.
- **Flash Messages**: User-friendly success/error notifications.
- **Secure Forms**: CSRF protection using **Flask-WTF**.

---

## Prerequisites

Before running the project, make sure you have:

- **Python 3.10** or above installed.
- **pip** (Python package manager).
- The following Python packages installed (can be installed via `requirements.txt`):
  - Flask
  - Flask-SQLAlchemy
  - Flask-Login
  - Flask-WTF
  - Werkzeug

---

## Installation & Setup

1. **Clone the repository** (or download the project folder):

```bash
git clone <repository_url>
cd paper_portal

2. Create a virtual environment (recommended):

python -m venv venv

3. Activate the virtual environment:

Windows:

venv\Scripts\activate

4. Install dependencies:

pip install -r requirements.txt

5. Run the Flask app:

python app.py

6. Access the application:

Open your web browser and go to:

http://127.0.0.1:5000/

**Notes**

The first admin account should already be in the shared database. If not, you can create an admin by adding a user with the role Admin directly in the database or via a script.

Ensure uploaded paper files are placed in the designated uploads folder if using existing data.

**License**

This project is open-source and free to use for educational purposes.
```
