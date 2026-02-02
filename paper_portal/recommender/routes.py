from flask import Blueprint, render_template, redirect, url_for, flash, current_app, send_from_directory
from flask_login import login_required, current_user
from ..models import Paper
from ..extensions import db
from flask import request

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
from flask import request # request import karna padega

@recommender_bp.route('/review/<int:paper_id>/<action>', methods=['GET', 'POST']) # POST add kiya
@login_required
def review_paper(paper_id, action):
    paper = Paper.query.get_or_404(paper_id)
    
    if action == 'accept':
        paper.status = 'Accepted'
        paper.feedback = "Congratulations! Your paper meets our standards."
        flash('Paper Accepted!', 'success')
        
    elif action == 'reject':
        # Reject ke liye feedback form se aayega
        reason = request.form.get('reason') # HTML form se reason lo
        if not reason:
            flash('Please provide a reason for rejection.', 'warning')
            return redirect(url_for('recommender.dashboard'))
            
        paper.status = 'Rejected'
        paper.feedback = reason
        flash('Paper Rejected with feedback.', 'danger')

    db.session.commit()
    return redirect(url_for('recommender.dashboard'))

# -----------------
# Download Paper
# -----------------
@recommender_bp.route('/download/<filename>')
@login_required
def download_paper(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
