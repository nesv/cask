"""
user.py

This module holds the blueprint and database models for anything remotely
user-related.
"""
from bourbon import db
from flask import Blueprint

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(48), unique=True)
    email = db.Column(db.String(128), unique=True)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User {0}>".format(self.username)


user = Blueprint("user", __name__)
