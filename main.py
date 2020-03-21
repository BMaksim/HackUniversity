from aiohttp import web
import requests


routes = web.RouteTableDef()


async def DBconn():
    conn = psycopg2.connect("dbname='neprav-db' user='univ' host='127.0.0.1' port='5432' password='12348765'")
    cur = conn.cursor()
    return (conn, cur)

async def getBooks():
    url = "https://openlibrary.org/api/books?bibkeys=ISBN:0439785960"
    response = requests.get(url)
    return response.json()

@routes.get('/get')
async def getsomething(request):
#    conn, cur = await DBconn()
#    data = await request.json()
    data = getBooks()
    return web.json_response(data)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, path="127.0.0.1", port="8080")


