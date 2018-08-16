from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.response import Response

class RestEndpoint(Endpoint):
	path = '/bots/{bid}'
	types = {'bid': 'snowflake'}

	async def get(self, request, bid):
		return Response(200, {})