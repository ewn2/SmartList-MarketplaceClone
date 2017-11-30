from flask import Flask, render_template, flash, url_for, session, request, abort
import sqlite3



app = Flask(__name__)

db = sqlite3.connect('backbone.db', check_same_thread=False)
cursor = db.cursor()

@app.route("/")
def main():
        return render_template("Login.html")
@app.route("/frontpage", methods=['GET', 'POST'])
def frontpage():
    Username = ""
    Password = ""
    User_db = sqlite3.connect('backbone.db',check_same_thread=False)
    find_user = ("SELECT * FROM Accounts WHERE userid = ? AND password = ?") 
    cursor.execute(find_user, [(userid),(password)])
    results = cursor.fetchall()
    
    if results:
        for i in results:
            print ("Welcome")
        return ("exit")
    return render_template("Login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    error = None; 
    username = ""
    password = ""
    cursor.execute('SELECT * FROM Accounts')
    if request.method == 'POST':
        cursor.execute("PRAGMA busy_timeout = 10000")

        User_db = sqlite3.connect('backbone.db',check_same_thread=False)
        add_cursor = User_db.cursor()
        Username = request.form['userid']
        Password = request.form['password']
        
        add_cursor.execute('''INSERT INTO user(userid, password) Values (?,?)''', ( Username, Password))
        User_db.commit()
        User_db.close()
        success = "Successfully added to database"
        return render_template('signin.html', success = success)
    return render_template("signin.html")

@app.route("/homepage")
def mainmenu():
    return render_template("Homepage.html")