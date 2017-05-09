from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField
from wtforms.validators import DataRequired


class ChildForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    birth_date = DateField('birth_date', validators=[DataRequired()])
    child_image = FileField('child_image', validators=[
        FileAllowed(UploadSet('images', IMAGES), 'Must be an image file.')
    ])
