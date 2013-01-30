#!/usr/bin/env python
#
# Bourbon is a Flask-powered content management system.
#
from argparse import ArgumentParser
from flask import Flask
import os


bourbon = Flask(__name__.split(".")[0])


@bourbon.route("/")
def home():
    """The index page for Bourbon."""
    return "Grab your flask of bourbon, and have at it!"


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--settings", default="settings.py",
                        dest="settings_module",
                        help="The Python file containing the settings.")
    parser.add_argument("--host", default="127.0.0.1:8008", dest="host",
                        help="The IPv4 address and port to listen on.")
    args = parser.parse_args()

    host, port = args.host.split(":")

    bourbon.config.from_pyfile(args.settings_module)
    bourbon.run(host=host, port=int(port))
