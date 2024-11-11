from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    image = FileField('Imagen', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    submit = SubmitField('Enviar')
