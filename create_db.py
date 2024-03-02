import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('DROP TABLE database')

cur.execute("""CREATE TABLE database (
          entry_num INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          real_id INTERGER NOT NULL UNIQUE,
          points INTERGER NOT NULL
) """)

preexisting_data = [
    (1,'Steve Smith', 211, 80),
    (2,'Jian Wong', 122, 92),
    (3,'Chris Peterson', 213, 91),
    (4,'Sai Patel', 524, 94),
    (5,'Andrew Whitehead', 425, 99),
    (6,'Lynn Roberts', 626, 90),
    (7,'Robert Sanders', 287, 75)
]

cur.executemany("INSERT INTO database VALUES (?, ?, ?, ?)", preexisting_data)

conn.commit()
conn.close()