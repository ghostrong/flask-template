from flask import Blueprint

comp2 = Blueprint('comp2',
                  __name__,
                  template_folder='templates',
                  static_folder='static'
                 )

from . import views
