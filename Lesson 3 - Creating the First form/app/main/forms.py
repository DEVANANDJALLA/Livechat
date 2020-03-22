from flask_wtf import FlaskForm
#from wtforms.fields import StringField, SubmitFields
from wtforms.fields import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required,Email, DataRequired

class LoginForm(FlaskForm):
    """Accepts email and password for verification"""
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')