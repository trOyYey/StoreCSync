#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models import *
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/SCS', strict_slashes=False)
def SCS():
    """ SCS main entry """
    catagories = storage.all("Catagory").values()
    catagories = sorted(catagories, key=lambda k: k.name)
    return render_template('index.html',
                           catagories=catagories)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
