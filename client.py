#!/usr/bin/env python3

'''
Python aiohttp example client .

Example developed on a BeagleBone Black running Debian 10.

Author: Kevin Partin
Email: kevin dot partin at gmail dot com
'''

import aiohttp
import asyncio

API_HOST = '127.0.0.1'
API_PORT = 8080
API_URI  = 'http://' + API_HOST + ':' + str(API_PORT)

async def main(uri: str):

    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html)

name = input('Enter your name: ')
uri = API_URI + '/'+ name
asyncio.run( main(uri) )
