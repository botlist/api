from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.redirect import Redirect


class RestEndpoint(Endpoint):
    path = '/auth/login'

    @property
    def discord(self):
        return self.server.discord

    async def get(self, request):
        session = await self.server.get_session(request)

        parameters = self.discord.generate_parameters('identify')
        session['state'] = parameters['state']
        print(session, session['state'])

        return Redirect(302, self.discord.authorize_url, parameters)