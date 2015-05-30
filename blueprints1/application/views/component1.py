from flask import Blueprint, render_template

comp1 = Blueprint('comp1', __name__)

@comp1.route('/')
def index():
    return render_template('component1/index.html')
