import sqlite3
conn = sqlite3.connect('backbone.db')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Accounts''')
cur.execute('''CREATE TABLE Accounts
             (userid text, password text, email text, phone text, PRIMARY KEY (userid))''')

cur.execute('''DROP TABLE IF EXISTS Listings''')
cur.execute('''CREATE TABLE Listings
             (userid text, ListingName text, AskingPrice money, Description text, ListTime timestamp, Picture varbinary(8000), FOREIGN KEY (userid) REFERENCES Accounts(userid) ON DELETE CASCADE)''')

conn.commit()
cur.close()
conn.close()
