#!/usr/bin/env python

from argparse import ArgumentParser
from bourbon import app
import os

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--settings", default="settings.py",
                        dest="settings_module",
                        help="The Python file containing the settings.")
    parser.add_argument("-a", "--listen-address", default="127.0.0.1:8008", 
                        dest="address",
                        help="The IPv4 address and port to listen on.")
    args = parser.parse_args()

    host, port = args.address.split(":")

    # Load the configurations in.
    app.config.from_pyfile("{0}/{1}".format(os.getcwd(), args.settings_module))

    # Finally, run the app.
    app.run(host=host, port=int(port))
