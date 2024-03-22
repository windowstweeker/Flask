from flask import render_template, request, Blueprint, current_app
from FlaskProject.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    with current_app.app_context():
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title='About')
