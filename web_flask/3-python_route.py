#!/usr/bin/python3
"""A Script that starts a simple Flask Web Application"""
from flask import Flask, request

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
