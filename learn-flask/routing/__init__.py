from flask import Flask, request, abort, render_template
from flask_wtf import Form
from wtforms import BooleanField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.debug = True
app.testing = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

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

class HelloForm(Form):
    name = StringField('name', validators=[DataRequired()])

@app.route('/helloform', methods=['GET', 'POST'])
def helloform():
    form = HelloForm()
    return render_template('helloform.html', form=form)

class HelloFields(Form):
    boolean_field = BooleanField('Boolean')
    select_field = SelectField('Select', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    string_field = StringField('String')
    text_area_field = TextAreaField('Text area')
    submit_field = SubmitField('Submit')

@app.route('/hellofields', methods=['GET', 'POST'])
def hellofields():
    form = HelloFields()
    return render_template('hellofields.html', form=form)

if __name__ == '__main__':
    app.run()
