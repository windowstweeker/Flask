from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from FlaskProject.config import Config
"""
re ordering things.  moving db below bootstrap

"""

# Initialize Bootstrap
bootstrap_version = 'latest'
if bootstrap_version == 'latest':
    from flask_bootstrap import Bootstrap5
    bootstrap = Bootstrap5()
else:
    from flask_bootstrap import Bootstrap4
    bootstrap = Bootstrap4()

# Initialize bcrypt for password hashing
bcrypt = Bcrypt()

# Initialize database
db = SQLAlchemy()

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Initialize mail for password reset
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # import instance of the blueprint
    from FlaskProject.users.routes import users
    from FlaskProject.posts.routes import posts
    from FlaskProject.main.routes import main
    from FlaskProject.errors.handlers import errors
    # register instance of the plueprint
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


"""
Look into the bootstrap 5 documentation.  It looks like there is a bunch of pre defined layouts like side bars
and nav bars.  Does it have a tool where you can use a toolbox and draw it out and color it/shape it in a cad way
and then it spits out html...

In series the blueprints look sick as fuck, restart to hear the description.. Check if available layout can be used 
without flask for other projects..  how it imports looks amazing. 

Once happy update everything to be a true template and write a quick how to update to a new projecct
archive and zip .. then start the work project...

"""
