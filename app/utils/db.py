import sqlite3   #enable control of an sqlite database
from utils.response import Response

DB_FILE="database.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def initializeUsersTable():
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY,
    username TEXT,
    displayName TEXT,
    password TEXT,
    UNIQUE (username))''')
    c.execute('''CREATE TABLE IF NOT EXISTS reminders(
    ID INTEGER PRIMARY KEY,
    username TEXT,
    reminderDesc TEXT,
    dueDate TEXT,
    isCompleted INTEGER
    )''')

def initializeDatabase():
    initializeUsersTable()

# AUTH
def addUser(username, displayName, password):
    '''Adds a new user into the database.'''
    try:
        c.execute("INSERT INTO users (username, displayName, password) VALUES(? , ?, ?)", (username, displayName, password))
        db.commit()
        return Response(True, True, "")

    except Exception as err:
        return Response(False, None, err)

def getUserByUsername(username):
    '''Gets the info of user based on username.'''
    try:
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        data = c.fetchone()

        res = {"id": data[0], "username": data[1], "displayName": data[2], "password": data[3],}

        return Response(True, res, "")
    except Exception as err:
        return Response(False, None, err)

def addReminder(username, reminderText, dueDate):
    '''Adds a new reminder, given an username, reminder text, and due date input.'''
    try:
        c.execute('INSERT INTO reminders (username, reminderDesc, dueDate, isCompleted) VALUES(?, ?, ?, ?)', (username, reminderText, dueDate, 0))
        db.commit()
        return Response(True, None, "")
    except Exception as err:
        return Response(False, None, err)
