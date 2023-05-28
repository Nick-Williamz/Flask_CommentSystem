# This will auth blueprint will be used to handle all of our authentication routes.

# Path: app\blueprints\auth.py
# first we'll import the Blueprint class from the flask package
from flask import Blueprint, render_template, redirect, url_for

# next we'll create an instance of the Blueprint class

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@bp.route('/logout')
def logout():
    # redirect to the home page
    return redirect(url_for('main.index'))
