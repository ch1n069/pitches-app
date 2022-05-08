from flask import render_template,redirect,url_for,abort
from app import app
from .auth import forms 





#views

@app.route('/')
def index():

    '''The home page of the application'''



    return render_template('index.html')


@app.route('/register')
def register():
    forms = RegistrationForm()
    return render_template('register.html', title='Register', forms=forms)
    

@app.route('/login')
def login():
    forms = LoginForm()
    return render_template('login.html', title='login', forms=forms)
    