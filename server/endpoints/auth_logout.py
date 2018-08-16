from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.response import Response

class RestEndpoint(Endpoint):
	path = '/auth/logout'

	async def post(self, request):
		return Response(200, {})