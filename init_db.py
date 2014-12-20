
import sqlite3
conn = sqlite3.connect('cheeps.db')
c = conn.cursor()
c.execute("CREATE TABLE cheeps (name, datetime, cheep)")
c.execute("INSERT INTO cheeps VALUES ('suzy', '100', 'Hello world!')")
c.execute("INSERT INTO cheeps VALUES ('bob', '100', 'Hi suzy!')")
c.execute("SELECT * FROM cheeps")
print(c.fetchall())
conn.commit()
conn.close()
