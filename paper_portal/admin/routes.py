from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import User, Paper
from ..extensions import db

admin_bp = Blueprint('admin', __name__)

# -----------------
# Dashboard
# -----------------
@admin_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'Admin':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    users = User.query.all()
    papers = Paper.query.all()
    return render_template('admin_dashboard.html', users=users, papers=papers)

# -----------------
# Change User Role
# -----------------
@admin_bp.route('/user/<int:user_id>/role/<new_role>')
@login_required
def change_role(user_id, new_role):
    if current_user.role != 'Admin':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    user = User.query.get_or_404(user_id)
    if new_role not in ['Publisher', 'Recommender', 'Admin']:
        flash("Invalid role.", "danger")
        return redirect(url_for('admin.dashboard'))
    
    user.role = new_role
    db.session.commit()
    flash(f"User {user.username} role changed to {new_role}.", "success")
    return redirect(url_for('admin.dashboard'))

# -----------------
# Delete User
# -----------------
@admin_bp.route('/user/<int:user_id>/delete')
@login_required
def delete_user(user_id):
    if current_user.role != 'Admin':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.username} deleted.", "success")
    return redirect(url_for('admin.dashboard'))

# -----------------
# Delete Paper
# -----------------
@admin_bp.route('/paper/<int:paper_id>/delete')
@login_required
def delete_paper(paper_id):
    if current_user.role != 'Admin':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    paper = Paper.query.get_or_404(paper_id)
    db.session.delete(paper)
    db.session.commit()
    flash(f"Paper '{paper.title}' deleted.", "success")
    return redirect(url_for('admin.dashboard'))
