from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, UserInput
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_behind_proxy import FlaskBehindProxy
#import yahoo_project
#from yahoo_project import AppleAmazon.png
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ede080d803e9f6d30ce3348400e0b49b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
proxied = FlaskBehindProxy(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    
class Searchs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(20), unique=True, nullable=False)
    start = db.Column(db.String(20), nullable=False)
    finish = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"Searchs('{self.stock}', '{self.start}', '{self.finish}')"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        bcrypt.check_password_hash(pw_hash, form.password.data) # returns True
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('user', name = form.username.data)) # if so - send to specific page
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<name>')
def user(name):
    return render_template('user_page.html', subtitle='Hello, ' + name + '!', text='Welcome to your personalized stock page. To add more stock information click the button below.')

folder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = folder

@app.route("/graphs")
def yahoo_page():
    graph = os.path.join(app.config['UPLOAD_FOLDER'], 'AppleAmazon.png')
    return render_template("yahoo.html", user_image = graph)

    
@app.route("/selection", methods=['GET', 'POST'])
def user_selection():
    form = UserInput()
    if form.validate_on_submit(): # checks if entries are valid
        search = Searchs(stock=form.stock.data, start=form.start.data, finish=form.finish.data)
        db.session.add(search)
        db.session.commit()
        flash(f'Looking data for {form.stock.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('user_choice.html', title='Selection', form=form)  
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")