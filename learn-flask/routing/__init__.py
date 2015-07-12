from flask import Flask, request, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/helloworld')
def helloworld():
    return 'Hello, World!'

@app.route('/hellovariable/<name>')
def hellovariable(name):
    return 'Hello, %s!' % name

@app.route('/hellotemplate')
def hellotemplate():
    return render_template('message.html', text=('Lorem ipsum dolor sit amet, '
                                                 'consectetur adipiscing elit, '
                                                 'sed do eiusmod tempor incididunt '
                                                 'ut labore et dolore magna aliqua.'))

@app.route('/hellopost', methods=['POST'])
def hellopost():
    if not request.form.get('name'):
        abort(400)
    return 'Hello, %s!' % request.form['name']

if __name__ == '__main__':
    app.run()
