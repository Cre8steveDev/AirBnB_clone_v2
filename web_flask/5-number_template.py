#!/usr/bin/python3
"""A Script that starts a simple Flask Web Application"""
from flask import Flask, request, abort, render_template

app: Flask = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns a View that displays "Hello HBNB! For the root URL route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a View that displays "HBNB" for the /hbnb URL route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Returns a View that displays "C" followed value of text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Returns a View that displays "Python" followed value of text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Returns a view that displays  'n is a number' only
    if n is an integer passed on the path"""

    try:
        num = int(n)
        return "{} is a number".format(num)
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Checks for odd and even and then return the value in a template"""
    try:
        num = int(n)
        return render_template('5-number.html', data=num)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
