import decimal
import json

from aiohttp.web import Response as AioHTTPResponse


class Response(AioHTTPResponse):
    def __init__(self, status, body=None, **kwargs):
        kwargs['status'] = status
        kwargs['content_type'] = kwargs.get('content_type', 'application/json').lower()

        headers = kwargs.pop('headers', {})
        headers['Access-Control-Allow-Headers'] = '*'
        headers['Access-Control-Allow-Methods'] = '*'
        headers['Access-Control-Allow-Origin'] = '*'
        kwargs['headers'] = headers

        super().__init__(**kwargs)
        if body is not None:
            if status == 204:
                body = None
            self.set_body(body, **kwargs)

    def set_body(self, body, content_type='application/json', charset=None, **kwargs):
        if content_type.startswith('application/json'):
            body = self.encode(body)
            charset = 'utf-8'

        if charset is not None:
            content_type = '; '.join([content_type, 'charset={}'.format(charset)])

        self.body = body
        self.content_type = content_type

    def filter(self, data):
        if data is None or isinstance(data, (bool, str)):
            return data
        elif isinstance(data, int) and data > 9007199254740991:
            data = str(data)
        elif isinstance(data, dict):
            for k in data:
                data[k] = self.filter(data[k])
        elif isinstance(data, (list, tuple)):
            for i in range(len(data)):
                data[i] = self.filter(data[i])
        elif isinstance(data, decimal.Decimal):
            data = float(data)

        return data

    def encode(self, data):
        return json.dumps(self.filter(data)).encode('utf-8')