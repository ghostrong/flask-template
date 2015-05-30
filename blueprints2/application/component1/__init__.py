from flask import Blueprint

comp1 = Blueprint('comp1',
                  __name__,
                  template_folder='templates',
                  static_folder='static'
                 )

from . import views
