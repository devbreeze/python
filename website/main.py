import os,binascii

from flask import Flask, render_template
from google.appengine.ext import ndb

class Config(ndb.Model):
    flask_debug = ndb.BooleanProperty(indexed=False)
    flask_secret_key = ndb.StringProperty(indexed=False)

results = Config.query().fetch(1)
config = results[0] if results else Config(flask_debug=True, flask_secret_key=binascii.b2a_hex(os.urandom(24))).put()

app = Flask(__name__)
app.config['DEBUG'] = config.flask_debug
app.config['SECRET_KEY'] = config.flask_secret_key

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
