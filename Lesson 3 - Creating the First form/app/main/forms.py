from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts email and password for verification"""
    email = StringField('email', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Enter Chatroom')