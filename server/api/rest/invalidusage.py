import api.rest.errors as errors

from api.rest.response import Response


class InvalidUsage(Response, Exception):
    def __init__(self, status=500, message=None, code=0, **kwargs):
        self.code = code

        if not message:
            message = errors.codes.get(code) if code else errors.http.get(status)
            if not message:
                status = 500
                message = errors.http.get(status)
        self.message = message

        Response.__init__(self, status, **kwargs)
        Exception.__init__(self, self.message)
        self.set_body(self.to_dict(), **kwargs)

    def to_dict(self):
        return {'status': self.status, 'code': self.code, 'message': self.message}