from flask import Flask

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object('config')

from views import *

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
