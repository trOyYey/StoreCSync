#!/usr/bin/python3
""" Starts a Flash Web Application SCS"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_SCS():
    """ Prints a Message when / is called """
    return 'Hello SCS!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
