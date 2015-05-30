from flask import Blueprint, render_template

comp2 = Blueprint('comp2', __name__)

@comp2.route('/')
def index():
    return render_template('component2/index.html')
