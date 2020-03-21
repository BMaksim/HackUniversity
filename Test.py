import psycopg2
import pandas as pd

# def DBconn():
#     conn = psycopg2.connect("dbname='hudb' user='univ' host='localhost' port='5432' password='12348765'")
#     cur = conn.cursor()
#     return (conn, cur)

# conn, cur = DBconn()
# cur.execute("SELECT * FROM books ORDER BY RANDOM() LIMIT 10")
# rows = cur.fetchall()
# print(rows)
# cur.close()
# conn.close()

bigTable = pd.read_excel("../priceext.xls")
table = pd.DataFrame({'Name': bigTable["Название"], 'Autor': bigTable["Автор"], 'Theme': bigTable["Тема"], \
                        'Price': bigTable["Розн.цена"], 'Image': bigTable["Изображение"]})
for i in range(5):
    some = [table.iloc[i, el] for el in range(5)]
    print("INSERT INTO books VALUES (nextval('hudb.public.books_id_seq'), {});".format(','.join(list(map(str,some)))))