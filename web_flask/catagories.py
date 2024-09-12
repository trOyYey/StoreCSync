#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/catagories', strict_slashes=False)
@app.route('/catagories/<catagory_id>', strict_slashes=False)
def states(catagory_id=None):
    """display the catagories and companies listed in alphabetical order"""
    catagories = storage.all("Catagory")
    if catagory_id is not None:
        catagory_id = 'Catagory.' + catagory_id
        print(f"{catagory_id}")
    return render_template('catagories.html', catagories=catagories, catagory_id=catagory_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
