# Paper Portal 📄

## Description
Paper Portal is a web-based academic paper submission and review system built with **Flask** and **Bootstrap 5**. 

It features a **tiered role system**:
1.  **Publisher (Default):** All new users start here. They can submit papers and view their status.
2.  **Recommender:** Publishers must **request an upgrade** (with proof of credentials) to become Recommenders. Once approved by an Admin, they can review, accept, or reject papers with feedback.
3.  **Admin:** Manages users, approves role promotion requests, and oversees the platform.

## 🚀 Features

### 👤 User Roles & Workflow
* **Publisher (Default Role)**
    * Register and login securely.
    * Submit academic papers (Title, Abstract, PDF/Docx upload).
    * View status of submitted papers (Pending, Accepted, Rejected).
    * **Request Upgrade:** Apply to become a Recommender by submitting a proof/bio.
* **Recommender (By Approval)**
    * View all papers pending review.
    * **Download Papers** to read content.
    * **Review System:** Accept papers or **Reject with Feedback** (Pop-up modal to explain reasons).
* **Admin**
    * **Dashboard:** Overview of all users and papers.
    * **Role Management:** Review and Approve/Reject promotion requests from Publishers.
    * Manual Role Control: Promote/Demote users manually.
    * Delete users or papers.

### 🛠 Core Functionalities
* **Secure Authentication:** Login, Logout, and Registration (Default: Publisher).
* **Role-Based Access Control (RBAC):** Routes are protected based on user roles.
* **Feedback Loop:** Publishers see exactly why a paper was rejected.
* **Responsive UI:** Clean, modern interface using Bootstrap 5.
* **Flash Messages:** Instant notifications for actions (Success/Error).

## 🛠 Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite, SQLAlchemy
* **Frontend:** HTML, CSS, Bootstrap 5 (CDN)
* **Authentication:** Flask-Login
* **Forms:** Flask-WTF

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd paper_portal
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * Windows: `venv\Scripts\activate`
    * Mac/Linux: `source venv/bin/activate`

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Initialize the Database:**
    Open a python shell in the project folder:
    ```python
    python
    >>> from paper_portal import create_app, db
    >>> app = create_app()
    >>> with app.app_context():
    ...     db.create_all()
    >>> exit()
    ```

6.  **Run the App:**
    ```bash
    python app.py
    ```

7.  **Access the Portal:**
    Open browser at: `http://127.0.0.1:5000/`

## 📝 Usage Guide

* **First Run:** The database is empty. Register a new user. 
* **Creating an Admin:** You need at least one Admin to approve requests. You can manually change a user's role to 'Admin' using a DB browser or Python script, or the first user can be set as Admin via code (if configured).
* **Workflow:**
    1.  User registers -> Role = **Publisher**.
    2.  Publisher submits a paper.
    3.  Publisher clicks "Become Recommender" -> Fills form.
    4.  Admin logs in -> Goes to "Requests" -> Clicks "Approve".
    5.  User is now **Recommender** -> Can review papers.

## 📜 License
This project is open-source and free to use for educational purposes.
