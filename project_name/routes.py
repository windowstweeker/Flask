from flask import render_template, url_for, flash, redirect
from project_name import app, db, bcrypt
from project_name.forms import RegistrationForm, LoginForm
from project_name.models import User, Post

posts = [
    {
        'author': 'Julian Feezell',
        'title': 'Blog Post 1',
        'content': 'First post blog',
        'date_posted': 'April 26, 1992'
    },
    {
        'author': 'Michelle Feezell',
        'title': 'Sailing Vacation',
        'content': 'My Last Post till America',
        'date_posted': 'April 10, 1912'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(User(username=form.username.data, email=form.email, password=hashed_password))
        #db.session.commit()
        with app.app_context():
            db.session.add(User(username=form.username.data, email=form.email, password=hashed_password))
        with app.app_context():
            db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)
