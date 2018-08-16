from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.response import Response

class RestEndpoint(Endpoint):
	path = '/users/@me'

	async def get(self, request):
		return Response(200, {'id': 'me'})