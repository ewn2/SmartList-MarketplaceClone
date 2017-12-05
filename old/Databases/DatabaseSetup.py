import sqlite3
conn = sqlite3.connect('backbone.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS Accounts''')
c.execute('''CREATE TABLE Accounts
             (userid text, password text, email text, phone text, PRIMARY KEY (userid))''')

c.execute('''DROP TABLE IF EXISTS Listings''')
c.execute('''CREATE TABLE Listings
             (userid text, ListingName text, AskingPrice money, Description text, ListTime timestamp, Picture varbinary(8000), FOREIGN KEY (userid) REFERENCES Accounts(userid) ON DELETE CASCADE)''')

conn.commit()
c.close()
conn.close()
