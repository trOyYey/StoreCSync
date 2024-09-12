#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/companies_by_catagories', strict_slashes=False)
def companies_by_catagories():
    """display the catagories and companies listed in alphabetical order"""
    catagories = storage.all("Catagory").values()
    return render_template('companies.html', catagories=catagories)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
