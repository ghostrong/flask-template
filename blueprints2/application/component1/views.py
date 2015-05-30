from flask import render_template
from . import comp1

@comp1.route('/')
def index():
    return render_template('index.html')
