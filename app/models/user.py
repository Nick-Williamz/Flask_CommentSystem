# This will serve as our user model.
# Path: app\models\user.py

# first we'll import the db object from the app package
from app import db
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from app import login_manager
from datetime import datetime

# next we'll create a class for the user model
# this class will inherit from the db.Model class
# this class will represent the users table in the database

class User(UserMixin, db.Model):
    # next we'll define the columns for the table
    # first we'll define the id column
    id = db.Column(db.Integer, primary_key=True)
    # next we'll define the username column
    username = db.Column(db.String(64), index=True, unique=True)
    # next we'll define the email column
    email = db.Column(db.String(120), index=True, unique=True)
    # next we'll define the password column
    password_hash = db.Column(db.String(128))
    email_confirmed = db.Column(db.Boolean, default=False)
    # next we'll define a method to set the password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    # next we'll define a method to check the password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # next we'll define a method to return a string representation of the user model
    def __repr__(self):
        return '<User {}>'.format(self.username)

