import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    #for reset password mail
    MAIL_SERVER='in-v3.mailjet.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True

    #using environment variables
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')

