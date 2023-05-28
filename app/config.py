# This will serve as the apps main configuration file.
# We'll add our secret key, database URI, and mail server settings here.

import os

# first we'll set up a base directory for the app
basedir = os.path.abspath(os.path.dirname(__file__))
# this will allow us to set up a relative path to the database file

# next we'll set up a class to store all the configuration variables
class Config(object):
    # first we'll set up the secret key
    # this is used to protect against CSRF attacks.
    SECRET_KEY = os.environ.get("CSRF_KEY")

    # next we'll set up the database URI
    # this is the location of the database file
    # we'll use SQLite for this project
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

    # this will signal the application every time a change is about to be made to the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
