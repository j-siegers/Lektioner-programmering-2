from flask import Flask
from markupsafe import escape
from flask import url_for, abort, redirect, render_template, session, request

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    return redirect(url_for('hello'))


@app.route('/login')
def login():
    abort(401)
