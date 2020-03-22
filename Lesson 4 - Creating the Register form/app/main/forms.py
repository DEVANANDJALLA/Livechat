from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Email, DataRequired, InputRequired,EqualTo

class LoginForm(FlaskForm):
    """Accepts email and password for verification"""
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Register')

