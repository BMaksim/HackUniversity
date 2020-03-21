import psycopg2

def DBconn():
    conn = psycopg2.connect("dbname='hudb' user='univ' host='localhost' port='5432' password='12348765'")
    cur = conn.cursor()
    return (conn, cur)

conn, cur = DBconn()
cur.execute("SELECT * FROM books ORDER BY RANDOM() LIMIT 10")
rows = cur.fetchall()
print(rows)
cur.close()
conn.close()