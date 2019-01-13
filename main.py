import os

import werkzeug
from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
@app.route('/resume.html')
@app.route('/profile.html')
def profile():
    return render_template('profile.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/project.html')
def project():
    return render_template('project.html')


@app.route('/_t_header.html')
def header():
    return render_template('_t_header.html')


@app.route('/_t_footer.html')
def footer():
    return render_template('_t_footer.html')


@app.errorhandler(Exception)
def error_internal_server(e):
    return render_template("_error.html", errorCode=e)


@app.route('/e404')
def e404():
    abort(404)


@app.route('/e500')
def e500():
    abort(500)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
else:
    print("is being imported into another module")
