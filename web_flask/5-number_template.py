#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """web app that displays 'Hello HBNB' at route:'/' """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_route():
    """ web app that displays 'HBNB' at route:'/hbnb' """
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """/c/<text>: , followed by value of the text variable
(replace underscore _ symbols with a space)"""
    return "C " + text.replace("_", " ")


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """/python/<text>: , followed by value of the
text variable (replace underscore _ symbols with a space )"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number_route(n):
    """/number/<n>: n is a  only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """/number_template/<n>: display a HTML page only if n is an integer:
H1 Number:  inside the tag BODY"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()ntag: numberdisplay Python display C display 
