from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from wtforms import TextAreaField

class PaperForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    abstract = TextAreaField('Abstract', validators=[DataRequired()])
    file = FileField('Upload Paper', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc', 'docx'], 'Documents only!')
    ])
    submit = SubmitField('Submit Paper')


class RecommenderRequestForm(FlaskForm):
    proof = TextAreaField('Why should you be a Recommender? (Qualifications/Links)', validators=[DataRequired()])
    submit = SubmitField('Send Request')