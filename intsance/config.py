import os


class Config(object):
    """
    Common configurations
    """

    POSTGRES = {
        'user': 'postgres',
        'pw': 'ANUbis4me',
        'db': 'Database1',
        'host': 'localhost',
        'port': '5432',
    }

    MYSQL = {
        'user': 'root',
        'pw': 'ANUbis4me',
        'db': 'database1',
        'host': 'localhost',
        'port': '3306'
    }

    MONGO = {
        'user': 'root',
        'pw': '',
        'db': 'database1',
        'host': 'localhost',
        'port': '27017'
    }

    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

    SECRET_KEY = 'b=3=!0^96*8jhkvkfbqf*1!yn-9'

    MONGO_DBNAME = 'database1'

    MONGO_URI = 'mongodb://{host}:{port}/{db}'.format(**MONGO)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)

    SQLALCHEMY_BINDS = {
        'postgres_bind': SQLALCHEMY_DATABASE_URI,
        'mysql_bind': 'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}'.format(**MYSQL),
        'sqlite_bind': 'sqlite:///database1.sqlite'
    }


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
