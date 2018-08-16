import inspect

from aiohttp.web import Request

from api.rest.response import Response
from api.rest.invalidusage import InvalidUsage

DEFAULT_METHODS = ('get', 'post', 'put', 'patch', 'delete', 'options', 'head')

class Endpoint:
	path = None
	types = {}
	def __init__(self, server):
		self.server = server

	def validate(self, data, typeof=dict, required=[]):
		if not isinstance(data, typeof):
			raise InvalidUsage(400)
		for key in required:
			if data.get(key) is None:
				raise InvalidUsage(400)
		return data

	async def options(self, request):
		return Response(204)

	async def dispatch(self, request: Request):
		method = request.method.lower()
		if method not in DEFAULT_METHODS:
			raise InvalidUsage(405)
		method = getattr(self, method, None)
		if not method or not callable(method):
			raise InvalidUsage(405)

		args_wanted = list(inspect.signature(method).parameters.keys())
		args_available = request.match_info.copy()
		args_available.update({'request': request})

		args_unsatisfied = set(args_wanted) - set(args_available.keys())
		if args_unsatisfied:
			raise InvalidUsage(400)

		for arg in self.types:
			if arg not in args_wanted:
				continue

			if self.types[arg] == 'snowflake':
				try:
					args_available[arg] = int(args_available[arg])
				except:
					raise InvalidUsage(400, '{} is not a snowflake'.format(arg))

		return await method(**{arg: args_available[arg] for arg in args_wanted})