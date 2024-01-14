class BaseConfig(object):
    SECRET_KEY = "Base random secret key"
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = "my default value"


class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = open("secret.txt").read()


class StagingConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "Another random development secret key"