import pandas as pd
import psycopg2
import random


bigTable = pd.read_excel("../priceext.xls")
table = pd.DataFrame({'Name': bigTable["Название"], 'Autor': bigTable["Автор"], 'Theme': bigTable["Тема"], \
                        'Price': bigTable["Розн.цена"], 'Image': bigTable["Изображение"]})
marks = [round(random.random()*10, 1) for i in range(len(table))]
table['Mark'] = marks
images = pd.Series(table["Image"])
del table["Image"]
table["Image"] = images
themes = ['Энциклопедии', 'Учебная и обучающая литература'] 
try:
    conn = psycopg2.connect("dbname='hudb' user='univ' host='localhost' port='5432' password='12348765'")
    cur = conn.cursor()
except:
    print("I am unable to connect to the database")

for i in range(len(table)):
    if table['Theme'][i] in themes:
        try:
            data = [table.iloc[i, el] for el in range(6)]
            cur.execute("INSERT INTO books VALUES (nextval('hudb.public.books_id_seq'), '{}');".format("','".join(list(map(str,data)))))
            conn.commit()
        except:
            continue    
    else:
        continue
cur.close()
conn.close()