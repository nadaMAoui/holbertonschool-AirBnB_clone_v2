#!/usr/bin/python3
"""
Flask web application that retrieves a list of states from a database
and displays them in an HTML template
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def teardown_appcontext(self):
    """
    Closes the database session after each request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Retrieves all states from the database
    and passes them to the HTML template to generate an HTML response
    """
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
