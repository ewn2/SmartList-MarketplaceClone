import sqlite3
conn = sqlite3.connect('listings.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS user''')
c.execute('''CREATE TABLE user
             (userid text, password text, PRIMARY KEY (userid))''')

c.execute('''DROP TABLE IF EXISTS junkdata''')
c.execute('''CREATE TABLE junkdata
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, spacefillingdata text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

conn.commit()
conn.close()