import jwt
import datetime
from FlaskProject import db, login_manager
from FlaskProject.config import Config
from flask import current_app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):  # class is = table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #  posts = db.relationship('Post', backref='author', lazy=True)
    posts = db.relationship('Post', backref=db.backref('author', lazy='joined'), lazy='dynamic')

    def get_reset_token(self, expires_sec=1800):
        reset_token = jwt.encode(
            {
                "user_id": self.id,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                       + datetime.timedelta(seconds=expires_sec)
            },
            Config['SECRET_KEY'],
            algorithm="HS256"
        )
        return reset_token


    @staticmethod
    def verify_reset_token(token):
        try:
            user_id = jwt.decode(
                token,
                Config['SECRET_KEY'],
                leeway=datetime.timedelta(seconds=10),
                algorithms=["HS256"]
            )
        except:
            return None
        return User.query.get(user_id.get('user_id'))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


#with current_app.app_context():
#db.create_all()

