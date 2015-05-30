from flask import Flask
from .views.component1 import comp1
from .views.component2 import comp2

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object('config')
app.register_blueprint(comp1, url_prefix='/comp1')
app.register_blueprint(comp2, url_prefix='/comp2')

from .views import *
