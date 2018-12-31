import os

from flask import Flask, render_template, request, redirect, url_for, session

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


@app.route('/header.html')
def header():
    return render_template('header.html')


@app.route('/footer.html')
def footer():
    return render_template('footer.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
else:
    print("is being imported into another module")
