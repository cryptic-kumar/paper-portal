from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class PaperForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    abstract = TextAreaField('Abstract', validators=[DataRequired()])
    file = FileField('Upload Paper', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc', 'docx'], 'Documents only!')
    ])
    submit = SubmitField('Submit Paper')
