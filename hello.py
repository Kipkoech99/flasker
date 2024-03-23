from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#create flask instance

app = Flask(__name__)
#secret key
app.config['SECRET_KEY'] = "Hahaaa"

#add database
#Old sqlite db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#New SQL db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password1234@localhost/our_users'

db = SQLAlchemy(app)
app.app_context().push()

#Create Model
class Users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(200), nullable=False)
    email = db.Column("email", db.String(200), nullable=False, unique=True)
    date_added = db.Column("date_added", db.DateTime, default=datetime.utcnow)

    #Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Create Form class
class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")



@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash('User Added Succesfully!')
    our_users = Users.query.order_by(Users.date_added)   
    return render_template('add_user.html', form=form, name=name, our_users=our_users)

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
