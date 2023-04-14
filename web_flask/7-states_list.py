#!/usr/bin/python3
"""
Flask web application that retrieves all states from a database and renders them in an HTML template
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """
    Closes the database session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Fetch all states from the database and
    render them in an HTML template
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
