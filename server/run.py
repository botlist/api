import asyncio
import json

import endpoints
from api.server import Server

with open('config.json') as cfile:
	config = json.load(cfile)

loop = asyncio.get_event_loop()

server = Server(loop=loop, **config)
loop.run_until_complete(server.initialize())
server.add_endpoints([getattr(endpoints, x) for x in endpoints.__all__], version=1, main=True)
server.run()