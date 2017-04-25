import os


class Config(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = 'fafuhiqwhf4h39hf4ihifhiuedwhqfase'

    # flask-social
    SOCIAL_FACEBOOK = {
        'consumer_key': '514463795395881',
        'consumer_secret': 'dc634805f71b04b4f3432f9986493c89'
    }

    # flask-mail
    MAIL_SERVER = 'replaceme' # TODO: Use something here
    MAIL_PORT = 25
    MAIL_DEFAULT_SENDER = 'vivi@derekperry.com'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass
