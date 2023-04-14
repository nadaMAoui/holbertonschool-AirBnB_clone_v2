#!/usr/bin/python3
"""Simple application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """Refresh data"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Fetch all states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
