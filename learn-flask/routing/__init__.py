from flask import Flask, request, abort, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return 'Hello, %s!' % name

@app.route('/factorial/<int:x>')
def factorial(x):
    return '%d! = %d.' % (x, math.factorial(x))

@app.route('/message')
def message():
    return render_template('message.html', text=('Lorem ipsum dolor sit amet, '
                                                 'consectetur adipiscing elit, '
                                                 'sed do eiusmod tempor incididunt '
                                                 'ut labore et dolore magna aliqua.'))

@app.route('/vote', methods=['POST'])
def vote():
    if not request.form.get('rating'):
        abort(400)
    try:
        rating = int(request.form['rating'])
    except ValueError:
        abort(400)
    if (rating < 0 or rating > 10):
        abort(400)
    return 'Thanks for Voting!'

if __name__ == '__main__':
    app.run()
