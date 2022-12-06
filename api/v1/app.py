#!/usr/bin/python3
""" Create app """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

host = getenv('HBNB_API_HOST', '0.0.0.0')
port = int(getenv('HBNB_API_PORT', '5000'))


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(error):
    """Close"""
    storage.close()

if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)