import settings

from werkzeug.contrib.fixers import ProxyFix
from flask import Flask
from flask import render_template, redirect, request, session
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
    ps = Post.objects().order_by("-publish_date")
    return render_template('index.html', posts=ps)


@app.route('/<string:post_slug>/')
def post(post_slug):
    p = Post.objects(slug=post_slug).first()
    return render_template('post.html', post=p)

if __name__ == '__main__':
    app.debug = settings.DEBUG
    app.secret_key = settings.SECRET
    app.run(host="0.0.0.0", port=settings.PORT)
