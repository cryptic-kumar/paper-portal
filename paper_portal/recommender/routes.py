from flask import Blueprint, render_template, redirect, url_for, flash, current_app, send_from_directory
from flask_login import login_required, current_user
from ..models import Paper
from ..extensions import db

recommender_bp = Blueprint('recommender', __name__)

# -----------------
# Dashboard
# -----------------
@recommender_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'Recommender':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    papers = Paper.query.filter_by(status='Submitted').all()
    return render_template('recommender_dashboard.html', papers=papers)

# -----------------
# View & Review Paper
# -----------------
@recommender_bp.route('/review/<int:paper_id>/<action>')
@login_required
def review_paper(paper_id, action):
    if current_user.role != 'Recommender':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    paper = Paper.query.get_or_404(paper_id)
    
    if action.lower() == 'accept':
        paper.status = 'Accepted'
    elif action.lower() == 'reject':
        paper.status = 'Rejected'
    else:
        flash("Invalid action.", "danger")
        return redirect(url_for('recommender.dashboard'))
    
    db.session.commit()
    flash(f"Paper '{paper.title}' has been {paper.status}.", "success")
    return redirect(url_for('recommender.dashboard'))

# -----------------
# Download Paper
# -----------------
@recommender_bp.route('/download/<filename>')
@login_required
def download_paper(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
