#!/usr/bin/python3
"""A Script that starts a simple Flask Web Application"""
from flask import Flask, request, abort, render_template
from models import storage
from models.state import State

app: Flask = Flask(__name__)


@app.teardown_appcontext
def tear_down(response_exception):
    """Function to be called after request has been handled or fails"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list(request):
    """Function to be called for matching string"""
    states = storage.all(State)
    all_states = [state for state in states]
    
    sorted_states = sorted(all_states, key=lambda state: state.name)
    
    return render_template('7-states_list.html', data=sorted_states)
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
