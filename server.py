#!/usr/bin/env python3

'''
Python aiohttp example server .

Example developed on a BeagleBone Black running Debian 10.

Author: Kevin Partin
Email: kevin dot partin at gmail dot com
'''

from aiohttp import web

async def handle(request: web.Request) -> web.Response:
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
])

if __name__ == '__main__':

    API_HOST = '127.0.0.1'
    API_PORT = 8080

    web.run_app(
        app  = app,
        host = API_HOST,
        port = API_PORT
    )
