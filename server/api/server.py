import asyncio
import time

from api.rest.router import Router

#from api.database import Database
from api.discord import Discord
from api.httpclient import HTTPClient
from api.snowflake import SnowflakeGenerator
from api.token import TokenGenerator

main_version = r'/v{version:\d+}'


class Server:
    def __init__(self, **kwargs):
        self.loop = kwargs.pop('loop', asyncio.get_event_loop())
        self.host = kwargs.pop('host', '127.0.0.1')
        self.port = kwargs.pop('port', 8000)
        self.proxied = kwargs.pop('proxied', False)
        self.base = kwargs.pop('base', '')

        self.snowflake = SnowflakeGenerator(**kwargs.pop('snowflake', {}))
        self.token = TokenGenerator(**kwargs.pop('token', {}))

        database_config = kwargs.pop('database', None)
        self.database = database_config  #and Database(loop=self.loop, config=database_config)

        self.httpclient = HTTPClient(loop=self.loop)
        self.discord = Discord(self, **kwargs.pop('discord', {}))

        self.router = Router(loop=self.loop, **kwargs.pop('aiohttp_server', {}))
        self.router.setup_session(kwargs.pop('session_token', None))

    @property
    def rest(self):
        return self.httpclient

    def get_session(self, request):
        return self.router.get_session(request)

    async def initialize(self):
        if self.database:
            await self.database.run()

    def add_endpoints(self, endpoints, version=None, main=False):
        base = self.base
        if version is not None:
            version = '/v{}'.format(version)

        for endpoint in endpoints:
            rest_endpoint = endpoint.RestEndpoint(self)
            paths = []

            path = rest_endpoint.path
            if not version and not main:
                paths.append(base + path)
            else:
                if version:
                    paths.append(base + version + path)
                if main:
                    paths.append(base + main_version + path)
                    paths.append(base + path)
            for path in paths:
                self.router.add(path, rest_endpoint)

    def run(self):
        self.router.on_shutdown(self.kill)
        self.router.run(self.host, self.port, proxied=self.proxied)

    async def kill(self, app):
        if self.database:
            await self.database.close()
        await self.httpclient.close()