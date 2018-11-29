import sqlite3

#conn = sqlite3.connect("test_sqlite.db")
conn = sqlite3.connect(':memory:')
curs = conn.cursor()

#curs.execute("CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)")

# curs.execute('INSERT INTO persons(name) values("Mike") ')


# curs.execute('INSERT INTO persons(name) values("Jun") ')
# curs.execute('INSERT INTO persons(name) values("Nancy") ')
#
#conn.commit()

# curs.execute('update persons set name = "Michel" where name = "Mike"')
# conn.commit()

#curs.execute('delete from persons where name = "Mike"')
conn.commit()
curs.execute("SELECT * from persons")
print(curs.fetchall())


curs.close()
conn.close()