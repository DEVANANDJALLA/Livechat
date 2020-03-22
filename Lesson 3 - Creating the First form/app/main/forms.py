from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    """Accepts email and password for verification"""
    email = StringField('Email', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')