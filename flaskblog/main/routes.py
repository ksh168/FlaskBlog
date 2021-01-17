from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
	#retrieve all posts from db
	#posts = Post.query.all()

	page = request.args.get('page', 1, type=int)	
	# setting type "int" so that it throws error if anyone tries to pass something 
	# other than integer in pg no.
	
	posts_ordered_by_latest_first = Post.query.order_by(Post.date_posted.desc())
	posts = posts_ordered_by_latest_first.paginate(page=page, per_page=5)

	return render_template('home.html', posts=posts)


@main.route("/about")
def about():
	return render_template('about.html', title='About')

