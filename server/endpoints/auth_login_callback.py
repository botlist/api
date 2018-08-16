from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.response import Response


class RestEndpoint(Endpoint):
    path = '/auth/login/callback'

    @property
    def discord(self):
        return self.server.discord

    async def get(self, request):
        session = await self.server.get_session(request)

        server_state = session.get('state')
        user_state = request.query.get('state')
        if server_state is None or user_state is None or str(server_state) != str(user_state):
            raise InvalidUsage(400, 'Invalid State')

        if request.query.get('error'):
            raise InvalidUsage(400, request.query.get('error'))
        if not request.query.get('code'):
            raise InvalidUsage(400, 'Missing Code')

        response = await self.discord.fetch_token('authorization_code', request.query.get('code'))

        if not response.ok:
            if response.is_json:
                raise InvalidUsage(response.status, response.data.error)
            else:
                raise InvalidUsage(400, 'Discord API Error')

        scope = response.data.scope.split(' ')
        if 'identify' not in scope:
            raise InvalidUsage(400, 'Invalid Scope')

        return Response(200, response.data)