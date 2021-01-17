import os
import secrets

from PIL import Image
from flask import url_for, current_app

from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)	#8 bytes
	_, f_ext = os.path.splitext(form_picture.filename)	#using _ as we don't need that(f_name) variable

	picture_filename = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)

	#resize image before saving
	output_size = (125, 125)		#size is 125x125
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	#now save it
	i.save(picture_path)

	return picture_filename


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request',
				sender='nimcham@protonmail.com', recipients=[user.email])
	
	msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
	mail.send(msg)
