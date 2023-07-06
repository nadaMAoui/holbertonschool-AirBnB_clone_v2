#!/usr/bin/python3
"""
You must use storage for fetching data
from the storage engine (FileStorage or DBStorage) =>
 from models import storage and storage.all(...)
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
        storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """etching data from the storage engine"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

