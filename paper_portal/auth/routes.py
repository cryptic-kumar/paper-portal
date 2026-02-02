from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import RegistrationForm, LoginForm
from ..models import User
from ..extensions import db, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# Login manager loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -----------------
# Registration
# -----------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('publisher.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw,
            role='Publisher'
        )
        db.session.add(user)
        db.session.commit()
        flash('Account created! You are now a Publisher.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

# -----------------
# Login
# -----------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.role == 'Publisher':
            return redirect(url_for('publisher.dashboard'))
        elif current_user.role == 'Recommender':
            return redirect(url_for('admin.dashboard'))
        elif current_user.role == 'Admin':
            return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for(f'{user.role.lower()}.dashboard'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    return render_template('login.html', form=form)

# -----------------
# Logout
# -----------------
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
