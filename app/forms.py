from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):
"""Contact form."""
	name = StringField(
	'Name',
	[DataRequired()]
	)
	email = StringField(
	'Email',
	[
	email(message=('not a valid email address.')),
	DataRequired()
	]
	)
	body = TextField(
    'Message',
    [
        DataRequired(),
        Length(min=4,
        message=('Your message is too short.'))
    ]
    )
recaptcha = RecaptchaField()
submit = SubmitField('Submit')