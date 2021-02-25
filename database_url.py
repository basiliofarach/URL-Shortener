import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS shortened_urls (id INTEGER PRIMARY KEY,orig_url TEXT, new_url VARCHAR(100) NOT NULL, UNIQUE (new_url))")
    conn.commit()
    conn.close()

def delete_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE shortened_urls")
    conn.commit()
    conn.close()

def insert(orig_url,new_url):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO shortened_urls (orig_url,new_url) VALUES (?,?)",(orig_url,new_url))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM shortened_urls")
    rows=cur.fetchall()
    conn.close()
    return rows

create_table()
print(view())
