from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp
from shop.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(),Regexp('^[a-z-0-9]{5,20}$',message='Your username should be between 5 and 20 characters long, and can contain lowercase letters or uppercase or numbers.')]) 
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^[a-z-0-9]{5,20}$',message='Your password should be between 5 and 20 characters long, and can  contain lowercase letters or uppercase or numbers'),EqualTo('confirm_password', message='Passwords do not match. Try again')])
  confirm_password=PasswordField('Confirm Password',validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username already exist. Please choose a different one.')



class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')
