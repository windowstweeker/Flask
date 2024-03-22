import os

path = os.path.dirname(__file__)

class Config(object):
    SECRET_KEY = 'SECRET_KEY'

    basedir = os.path.abspath(path)
    path = os.getcwd()

    """  Valid SQLite URL forms are:
            sqlite:///:memory: (or, sqlite://)
            sqlite:///relative/path/to/file.db
            sqlite:////absolute/path/to/file.db
    """
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'site.db')}"
    """
    set to environment variables and can have conditional to if production
    is unavailable default to a :memory: or a sqlite database
    """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{path}/site.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    MAIL_SERVER = 'smtp.gmail.com'

    mail_protocol = 'tsl'
    # mail_protocol = 'ssl'

    if mail_protocol == 'tsl':
        MAIL_USE_SSL = False
        MAIL_USE_TLS = True
        MAIL_PORT = 587
    elif mail_protocol == 'ssl':
        MAIL_USE_SSL = True
        MAIL_USE_TLS = False
        MAIL_PORT = 465

    # mail_credentials = 'hidden'
    mail_credentials = 'debug'

    if mail_credentials == 'hidden':
        """ Pass through the RSA for encryption Look at the decode/encode to utf-8 vs bin.  1 file vs 3 """
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    if mail_credentials == 'debug':
        MAIL_USERNAME = 'root'
        MAIL_PASSWORD = 'l33t'