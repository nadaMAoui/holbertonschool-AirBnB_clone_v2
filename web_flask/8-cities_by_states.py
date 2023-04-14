#!/usr/bin/python3
"""Flask web application that retrieves data from a database and displays it"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """Closes the database session after each request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Retrieve all the states and the cities
    in each state from the database and render them
    in a template for display on the web page.

    Returns:
        A Flask template rendered with data for all
        the states and cities in the database.
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
