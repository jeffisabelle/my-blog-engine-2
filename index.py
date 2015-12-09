import settings

from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, render_template, redirect, request, session
from flask.ext.superadmin import Admin, AdminIndexView

from models import Post

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


class AdminView(AdminIndexView):
    def is_accessible(self):
        return session.get("logged-in")


admin = Admin(app, index_view=AdminView())
admin.register(Post)


@app.route('/adm')
def adm():
    logged = session.get("logged-in")
    if logged:
        return redirect('/admin')
    else:
        return render_template('adm.html')


@app.route("/adm/login", methods=["POST"])
def adm_login():
    password = request.form["password"]

    if str(password) == str(settings.PASS):
        session["logged-in"] = True
        return redirect('/admin')
    else:
        return "error"


@app.route('/')
def index():
    posts = Post.objects().order_by("-publish_date")
    source = render_template('index.html', posts=posts)
    return render_template('index.html', source=source, posts=posts)


@app.route('/<string:post_slug>/')
def post(post_slug):
    p = Post.objects(slug=post_slug).first()
    source = render_template('detail-no-content.html', post=p)
    return render_template('detail.html', source=source, post=p)


if __name__ == '__main__':
    app.debug = settings.DEBUG
    app.secret_key = settings.SECRET
    app.run(host="0.0.0.0", port=settings.PORT)
