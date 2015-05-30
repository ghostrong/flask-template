from flask import Flask
from .component1 import comp1
from .component2 import comp2

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object('config')
app.register_blueprint(comp1, url_prefix='/comp1')
app.register_blueprint(comp2, url_prefix='/comp2')

from .component1 import views
from .component2 import views
