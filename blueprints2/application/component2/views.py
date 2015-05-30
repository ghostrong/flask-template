from flask import render_template
from . import comp2

@comp2.route('/')
def index():
    return render_template('index.html')
