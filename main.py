from aiohttp import web
import requests
import isbnlib
import psycopg2


routes = web.RouteTableDef()


async def DBconn():
    conn = psycopg2.connect("dbname='hudb' user='univ' host='localhost' port='5432' password='12348765'")
    cur = conn.cursor()
    return (conn, cur)


@routes.get('/get20')
async def get20(request):
    conn, cur = await DBconn()
    cur.execute("SELECT * FROM books ORDER BY RANDOM() LIMIT 20")
    rows = cur.fetchall()
    books = []
    for elem in rows:
        books.append({"Name": elem[1], "Autor": elem[2], "Theme": elem[3], "Price": elem[4], "Mark":elem[5], "Image":elem[6]})
    data = {"data": books}
    cur.close()
    conn.close()
    return web.json_response(data)

# @routes.get('/get')
# async def getsomething(request):


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, path="127.0.0.1", port="8080")
