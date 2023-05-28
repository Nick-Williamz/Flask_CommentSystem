# This will be the blueprint for comment routes.
# Path: app\blueprints\comments.py

from flask import Blueprint, render_template

bp = Blueprint('comments', __name__)

# next we'll create a route for the comments page

@bp.route('/comments', methods=['GET', 'POST'])
def comments():
    return render_template('comments/comments.html')