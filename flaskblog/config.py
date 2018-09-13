""" Config File."""
import os


class Config:
    """ 
    import secrets
    secrets.token_hex(16)
    """
    SECRET_KEY = '25972dab4522897d30850351d9b878eb'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # os dois item acima devem estar nas variáveis de ambiente
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    """
    If got "smtplib.SMTPAuthenticationError":

    Gmail blocks your sign-in attempt since it is from an unsafe link. 
    Switch on the 'Allow less secure apps' option in gmail temporarily. 
    It should work.
    """
