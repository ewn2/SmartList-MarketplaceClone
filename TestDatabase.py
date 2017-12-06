import sqlite3
conn = sqlite3.connect('backbone.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS Accounts''')
c.execute('''CREATE TABLE Accounts
             (userid text not null, password text not null, sjsuid text not null, email text not null, phone text not null, id integer primary key autoincrement)''')

c.execute("INSERT INTO Accounts Values ('User1', 'one', 1, 'user1@email.com', 1234567890, 0)")
c.execute("INSERT INTO Accounts Values ('User2', 'two', 2, 'user2@email.com', 1234567890, 1)")
c.execute("INSERT INTO Accounts Values ('User3', 'three', 3, 'user3@email.com', 1234567890, 2)")
c.execute("INSERT INTO Accounts Values ('User4', 'four', 4, 'user4@email.com', 1234567890, 3)")
c.execute("INSERT INTO Accounts Values ('User5', 'five', 5, 'user5@email.com', 1234567890, 4)")

c.execute('''DROP TABLE IF EXISTS Listings''')
c.execute('''CREATE TABLE Listings
             (userid text, post INTEGER PRIMARY KEY AUTOINCREMENT, ListingName text not null, AskingPrice text, Description text, Picture text, Email text, Phone text, FOREIGN KEY (userid) REFERENCES Accounts(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO Listings Values('User1', 1, 'Blue Shoes', '60', 'Shoes that are blue', 'https://cdn5.kicksonfire.com/wp-content/uploads/2017/06/Air-Jordan-5-Blue-Suede-6-565x372.jpg?x76107', 'user1@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User1', 2, 'Red Shoes', '50', 'Shoes that are red', 'https://cdn5.kicksonfire.com/wp-content/uploads/2017/07/Air-Jordan-11-2-565x372.jpg?x76107', 'user1@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User1', 3, 'Science Textbook', '80', 'Old book I do not need anymore', 'https://i.pinimg.com/736x/46/b8/b4/46b8b419e0d0a571c4b88fe37da533b2--chemistry-textbook-books-for-sale.jpg', 'user1@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User2', 4, 'Blue Shoes', '90.99', 'Unworn', 'https://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=158112935', 'user2@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User2', 5, 'Math Textbook', '120.00', 'Business Calc book', 'http://www.larsoncalculus.com/images/book_covers/Calc-10e.png', 'user2@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User2', 6, 'Desk Lamp', '12.50', 'Also has a usb charger slot', 'https://img3.banggood.com/thumb/view/oaupload/banggood/images/08/D8/6c0063f6-5137-451c-a8f5-81ce2bc90eeb.jpg', 'user2@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User3', 7, 'Computer Mouse', '14', 'appearance worn but ability not affected', 'https://cdn.thewirecutter.com/wp-content/uploads/2016/09/wireless-mice-lowres-8560.jpg', 'user3@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User3', 8, 'Acoustic Guitar', '40', 'No time to play anymore', 'http://media.guitarcenter.com/is/image/MMGS7/GS-Mini-Mahogany-Acoustic-Guitar-Mahogany/H79318000001000-00-500x500.jpg', 'user3@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User3', 9, 'Patio Chair', '36.00', 'Moving, cannot take it with me', 'https://target.scene7.com/is/image/Target/15461084?wid=520&hei=520&fmt=pjpeg', 'user3@email.com', '123 456 7890')''')
c.execute('''INSERT INTO Listings Values('User4', 10, 'Old Smartphone', '100', 'Perfect working condition, does not come with charger', 'http://media.idownloadblog.com/wp-content/uploads/2012/02/white-iPhone-4s-510x343.jpg', 'user4@email.com', '123 456 7890')''')

conn.commit()
conn.close()