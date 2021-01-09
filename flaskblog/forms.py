from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flaskblog.models import User

class RegistrationForm(FlaskForm):
	#setting up username(it's a string, required field, length from 2 to 20 characters)
	username = StringField('Username', 
					validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
							 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		#raise error if username already exists
		if user:
			raise ValidationError('Username already exists')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		#raise error if email already exists
		if user:
			raise ValidationError('Email already registered')



class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')