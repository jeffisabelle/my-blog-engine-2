import settings

from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, render_template

# from models import Post
from posts import Post

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/')
def index():
    # posts = Post.objects().order_by("-publish_date")
    posts = Post.all()
    source = render_template('index.html', posts=posts)
    return render_template('index.html', source=source, posts=posts)


@app.route('/<string:post_slug>/')
def post(post_slug):
    p = Post.one(post_slug)
    source = render_template('detail-no-content.html', post=p)
    return render_template('detail.html', source=source, post=p)


if __name__ == '__main__':
    app.debug = settings.DEBUG
    app.secret_key = settings.SECRET
    app.run(host="0.0.0.0", port=settings.PORT)
