from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate user sessions
from flask import redirect
from os import urandom

from utils.auth import AuthService
from utils.db import *

app = Flask(__name__)

auth = AuthService()

@app.route("/")
def landingpage():
    '''If user is logged in, then returns the home page. Otherwise, render login page.'''
    currentUserResponse = auth.currentUser()

    if currentUserResponse.success:
        currentUser = currentUserResponse.data

        if currentUser: #Checks if user is logged in
            return "Hi, " + currentUser["displayName"] + "!"

    return render_template( 'login.html' ) # Render the login template


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''If user does a get request, then return the login page. If it is a post request aka user logs in from login page, then check user credentials and will log in or deny based on provided credentials.
    The requests property contains the values property.
    The value property contains data from both requests.args and requests.form.'''

    if request.method == "GET": #for when you refresh the website
        return redirect('/')
    else: #when you log in from /
        username = request.values['username']
        password = request.values['password']

        if auth.login(username, password).success:
            return redirect("/")
        else:
            return render_template('login.html', error='Incorrect username or password')

@app.route("/signup", methods=['GET', 'POST'])
def register():
    '''If user does a get request (presses signup link from login page), then return registration page. Otherwise, creates a new user and add it to database for future authentication uses.'''
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":  #Takes values entered by user via request.values
        username = request.values['username']
        displayName = request.values['displayName']
        password = request.values['password']

        registerResponse = auth.register(username, displayName, password) #Appends user info to a database

        if registerResponse.success:
            return redirect("/login") #After registering, brings you to login
        else:
            return render_template('register.html')


@app.route("/logout")
def logout():
    '''Logs currently logged in user out of session.'''
    auth.logout() #function to logout
    return redirect("/") #redirect to login page

if __name__ == "__main__": #false if this file imported as module
    initializeDatabase()
    app.secret_key = urandom(32) # randomized secret key
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
