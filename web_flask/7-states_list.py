#!/usr/bin/python3

from flask import Flask, render_template
from models import storage


"""
You must use storage for fetching data
from the storage engine (FileStorage or DBStorage) =>
from models import storage and storage.all(...)
"""


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage connection after each request.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Fetches data from the storage engine and renders the template.
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

