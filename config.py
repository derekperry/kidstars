import os


class Config(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = 'fafuhiqwhf4h39hf4ihifhiuedwhqfase'

    # flask-mail
    MAIL_SERVER = 'replaceme' # TODO: Use something here
    MAIL_PORT = 25
    MAIL_DEFAULT_SENDER = 'vivi@derekperry.com'

    # flask-sqlalchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # flask-security
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'frewqjaibhf24ib3qbib34ibfo34lf;lf3;q34;f34q;f43f'

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'].replace('postgres', 'postgresql+psycopg2')

    SOCIAL_FACEBOOK = {
        'consumer_key': os.environ['FB_CONSUMER_KEY'],
        'consumer_secret': os.environ['FB_CONSUMER_SECRET']
    }