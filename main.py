from aiohttp import web
import requests
import isbnlib
import psycopg2
from OCR import imageToText

routes = web.RouteTableDef()


async def DBconn():
    conn = psycopg2.connect("dbname='hudb' user='univ' host='localhost' port='5432' password='12348765'")
    cur = conn.cursor()
    return (conn, cur)

# Send information about 20 random books from DB
@routes.get('/get20')
async def get20(request):
    conn, cur = await DBconn()
    cur.execute("SELECT * FROM books ORDER BY RANDOM() LIMIT 20;") # Get 20 random row
    rows = cur.fetchall()
    books = []
    for elem in rows:
        books.append({"name": elem[1], "author": elem[2], "theme": elem[3], "price": elem[4], "mark":elem[5], "image":elem[6]})
    data = {"data": books}
    cur.close()
    conn.close()
    return web.json_response(data)

@routes.post('/image-handler')
async def imageHandler(request):
    data = await request.json()
#    img = data["image"]
    img = bytearray(data["image"])
    print(img)
    text = imageToText(img)
    data = {"data": text}
    return web.json_response(data)

@routes.post('/get-theme')
async def getTheme(request):
    data = await request.json()
    conn, cur = await DBconn()
    cur.execute("SELECT * FROM books WHERE theme='{}' ORDER BY RANDOM() LIMIT 10;".format(data["theme"]))
    rows = cur.fetchall()
    books = []
    for elem in rows:
        books.append({"name": elem[1], "author": elem[2], "theme": elem[3], "price": elem[4], "mark":elem[5], "image":elem[6]})
    data = {"data": books}
    cur.close()
    conn.close()
    return web.json_response(data)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, path="127.0.0.1", port="8080")
