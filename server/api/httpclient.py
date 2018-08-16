import aiohttp
import asyncio
import json
import sys

from urllib.parse import urlencode
from urllib.parse import quote as _uriquote


def urlquery(url, **parameters):
    return '{}:{}'.format(url, urlencode(parameters))


class Route:
    def __init__(self, method, url, **parameters):
        self.method = method
        if parameters:
            self.url = url.format(**{k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
        else:
            self.url = url


class Response:
    def __init__(self, response):
        self.status = response.status,
        self.is_json = bool(response.headers.get('content-type', '').lower().startswith('application/json'))
        self.data = None
        self.response = response

    @property
    def ok(self):
        return 200 <= self.status and self.status < 300

    async def fetch_data(self):
        data = await self.response.text(encoding='utf-8')
        if self.is_json and data:
            data = json.loads(data)
        self.data = data

        return self


class HTTPClient:
    def __init__(self, **kwargs):
        self.loop = kwargs.pop('loop', asyncio.get_event_loop())

        self._session = aiohttp.ClientSession(loop=self.loop)

        user_agent = 'botlist.gg (https://botlist.gg {}) Python/{} aiohttp/{}'
        self.user_agent = user_agent.format('0.0.1', sys.version_info, aiohttp.__version__)

    def recreate(self):
        if self._session.closed:
            self._session = aiohttp.ClientSession(loop=self.loop)

    async def close(self):
        if not self._session.closed:
            await self._session.close()

    async def _request(self, method, url, *args, **kwargs):
        headers = kwargs.pop('headers', {})
        headers.update({'User-Agent': self.user_agent})

        if 'json' in kwargs:
            headers['content-type'] = 'application/json'
            kwargs['data'] = json.dumps(kwargs.pop('json'))

        kwargs['headers'] = headers

        response = Response(await self._session.request(method, url, **kwargs))
        return await response.fetch_data()

    def request(self, route, *args, **kwargs):
        return self._request(route.method, route.url, *args, **kwargs)