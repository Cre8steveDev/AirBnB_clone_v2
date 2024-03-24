#!/usr/bin/python3
"""A Script that starts a simple Flask Web Application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns a View that displays "Hello HBNB! For the root URL route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a View that displays "HBNB" for the /hbnb URL route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
