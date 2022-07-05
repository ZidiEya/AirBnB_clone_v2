#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ followed by value of the text variable"""
    return ('C ' + text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_(text='is cool'):
    """", followed by value of text variable"""
    return ('Python ' + text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_(n):
    """n is a  only if n = a integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_(n):
    """ display the HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run()numberdisplay Python display C display 
