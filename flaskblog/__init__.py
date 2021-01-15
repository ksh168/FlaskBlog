import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = '0321cc841079e4673edee425dad8ddb6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
#for account page
login_manager.login_view = 'login'      #function name is passed here
login_manager.login_message_category = 'info'

#for reset password mail
app.config['MAIL_SERVER']='in-v3.mailjet.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True

#using environment variables
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')

mail = Mail(app)


#keep this line at last only
from flaskblog import routes