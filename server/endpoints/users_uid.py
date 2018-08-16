from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.response import Response

class RestEndpoint(Endpoint):
	path = '/users/{uid}'
	types = {'uid': 'snowflake'}

	async def get(self, request, uid):
		return Response(200, {})