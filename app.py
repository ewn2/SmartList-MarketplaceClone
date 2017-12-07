from flask import Flask, render_template, flash, url_for, session, request, abort
import sqlite3
from definer import definer


app = Flask(__name__)

db = sqlite3.connect('backbone.db', check_same_thread=False)
cursor = db.cursor()

# @ is a decorator which is a way to wrap a function and modifying its behavior
@app.route("/")
def main():
        return render_template("frontpage.html")
@app.route("/frontpage", methods=['GET', 'POST'])
def frontpage():
    Username = request.form['Username']
    Password = request.form['Password']
    User_db = sqlite3.connect('backbone.db',check_same_thread=False)
    cursor.execute("SELECT COUNT(1) FROM Accounts WHERE userid = %s;", [Username]) 
    if cursor.fetchone()[0]:
        cursor.execute("SELECT password FROM Accounts WHERE userid = %s;", [Username])
        for row in cursor.fetchall():
            if Password == row[0]:
                return render_template("mainmenu.html")
            else:
                flash("Invalid Login Information")
                return render_template("frontpage.html")

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
        Sjsuid = request.form['sjsuid']
        email = request.form['email']
        phone = request.form['phone']
        tempphone = phone.replace("-", " ").replace("(", " ").replace(")", " ")
        phone = tempphone.replace("  ", " ")
        add_cursor.execute('''INSERT INTO Accounts(userid, password, sjsuid, email, phone) Values (?,?,?,?,?)''', ( Username, Password, Sjsuid, email, phone))
        User_db.commit()
        User_db.close()
        success = "Successfully added to database"
        return render_template('signin.html', success = success)
    return render_template("signin.html") 

@app.route("/mainmenu")
def mainmenu():
    return render_template("mainmenu.html")

@app.route("/session")
def sessionhub():
    return render_template("SessionHub.html")

@app.route('/Listing', methods=['GET', 'POST'])
def basketball():
    ListingName = None
    AskingPrice = None
    Description = None
    Picture = None
    Email = None
    Phone = None

    cursor.execute('SELECT * FROM Listings')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        basketball_db = sqlite3.connect('backbone.db',check_same_thread=False)
        add_cursor = basketball_db.cursor()
        ListingName = request.form['ListingName']
        AskingPrice = request.form['AskingPrice']
        Description = request.form['Description']
        Picture = request.form['Picture']
        Email = request.form['Email']
        Phone = request.form['Phone']
        tempphone = Phone.replace("-", " ").replace("(", " ").replace(")", " ")
        Phone = tempphone.replace("  ", " ")
        add_cursor.execute('''INSERT INTO Listings(  
            ListingName, AskingPrice, Description, Picture, Email, Phone)
            Values(?,?,?,?,?,?)''', (
            ListingName, AskingPrice, Description, Picture, Email, Phone))
        basketball_db.commit()
        basketball_db.close()
        success = "Successfully added to database"
        return render_template('mainmenu.html', success=success)
    return render_template('Listing.html')
    
@app.route("/resulthub", methods=['GET', 'POST'])
def bballresults(currentview="basketball"):
    ID = None
    lname = None
    price = None
    desc = None
    plink = None
    email = None
    phone = None
    list_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from Listings")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            #FG = row[0] #user_id = None, why?
            ID = row[1] #primary key
            lname = row[2]
            price = row[3]
            desc = row[4]
            plink = row[5]
            email = row[6]
            phone = row[7]
            listi = definer(lname, price, desc, plink, email, phone)
            list_dict[ID] = listi #storing in Data Structure for printing purposes
        return render_template('ResultHub.html', ID=ID, list_dict=list_dict)
    return render_template("ResultHub.html")

if __name__ == "__main__":
	app.run(debug=True)
