from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, send_from_directory
from flask_login import login_required, current_user
from .forms import PaperForm
from ..models import Paper
from ..extensions import db
import os
from werkzeug.utils import secure_filename

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
