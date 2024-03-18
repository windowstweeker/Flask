from datetime import datetime
from project_name import app, db
from sqlalchemy.orm import Mapped, mapped_column

# class is = table


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    image_file: Mapped[str] = mapped_column(nullable=False, default='default.jpg')
    # posts = db.relationship('Post', backref='author', lazy=True)


"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    #def __init__(self, username, email, password):
    #    self.username = username
    #    self.email = email
    #    self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
"""


class Post(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, date_posted, content):
        self.title = title
        self.date_posted = date_posted
        self.content = content

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


with app.app_context():
    db.create_all()

with app.app_context():
    db.session.commit()
