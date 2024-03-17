from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create flask instance

app = Flask(__name__)
app.config['SECRET_KEY'] = "Hahaaa"

#Create Form class
class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


#create index route

@app.route('/')

def index():
    first_name = "Evans"
    stuff = "This is <strong>Bold</strong> text"
    return render_template("index.html", first_name=first_name, stuff=stuff)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

@app.errorhandler(404)

#invalid URL
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
#Internal server error
def server_error(e):
    return render_template("500.html"), 500

#create Name Page
@app.route('/name', methods=['GET', 'POST'])

def name():
    name = None
    form = NameForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Succesfully!")

    return render_template('name.html', name=name, form=form)



