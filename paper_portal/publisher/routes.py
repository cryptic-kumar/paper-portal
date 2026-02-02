from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, send_from_directory
from flask_login import login_required, current_user
from .forms import PaperForm
from ..models import Paper
from ..extensions import db
import os
from werkzeug.utils import secure_filename
from paper_portal.models import db, RoleRequest # Import add karein
from .forms import PaperForm, RecommenderRequestForm # Import update karein

publisher_bp = Blueprint('publisher', __name__)

# -----------------
# Dashboard
# -----------------
@publisher_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'Publisher':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    papers = Paper.query.filter_by(user_id=current_user.id).all()
    return render_template('publisher_dashboard.html', papers=papers)

# -----------------
# Submit Paper
# -----------------
@publisher_bp.route('/submit', methods=['GET', 'POST'])
@login_required
def submit_paper():
    if current_user.role != 'Publisher':
        flash("Access denied.", "danger")
        return redirect(url_for('auth.login'))
    
    form = PaperForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        
        paper = Paper(
            title=form.title.data,
            abstract=form.abstract.data,
            filename=filename,
            user_id=current_user.id
        )
        db.session.add(paper)
        db.session.commit()
        flash("Paper submitted successfully!", "success")
        return redirect(url_for('publisher.dashboard'))
    
    return render_template('submit_paper.html', form=form)

# -----------------
# Download Paper
# -----------------
@publisher_bp.route('/download/<filename>')
@login_required
def download_paper(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


@publisher_bp.route('/request-upgrade', methods=['GET', 'POST'])
@login_required
def request_upgrade():
    # Sirf Publisher hi request kar sakta hai
    if current_user.role != 'Publisher':
        flash('You are already a Recommender or Admin.', 'info')
        return redirect(url_for('publisher.dashboard'))

    # Check karein agar pehle se koi pending request hai
    existing_req = RoleRequest.query.filter_by(user_id=current_user.id, status='Pending').first()
    if existing_req:
        flash('You already have a pending request. Please wait for Admin approval.', 'warning')
        return redirect(url_for('publisher.dashboard'))

    form = RecommenderRequestForm()
    if form.validate_on_submit():
        new_req = RoleRequest(user_id=current_user.id, proof_text=form.proof.data)
        db.session.add(new_req)
        db.session.commit()
        flash('Request sent to Admin! Wait for approval.', 'success')
        return redirect(url_for('publisher.dashboard'))

    return render_template('request_upgrade.html', form=form)