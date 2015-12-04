import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>This is Home page</h1>')
async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', '8050')
    print('Server started at http://127.0.0.1:8050')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()