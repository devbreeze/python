from flask import Flask
from main import main
from admin import admin

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
