from api.httpclient import Route


class Discord:
    def __init__(self, server, **kwargs):
        self.server = server

        self.bot_id = kwargs.pop('bot_id', None)
        self.secret = kwargs.pop('secret', None)
        self.redirect_uri = kwargs.pop('redirect_uri', None)
        self.token_uri = kwargs.pop('token_uri', None)

    @property
    def rest(self):
        return self.server.rest

    @property
    def snowflake(self):
        return self.server.snowflake

    @property
    def authorize_url(self):
        return 'https://discordapp.com/api/oauth2/authorize'

    def generate_parameters(self, scope='identify', state=None):
        return {
            'scope': scope,
            'response_type': 'code',
            'client_id': self.bot_id,
            'state': state or self.snowflake.generate(),
            'redirect_uri': self.redirect_uri,
        }

    def fetch_user(self, token, user_id='@me'):
        return self.rest.request()

    async def fetch_token(self, grant_type='authorization_code', code=None, refresh_token=None):
        data = {
            'client_id': self.bot_id,
            'client_secret': self.secret,
            'grant_type': grant_type,
            'redirect_uri': self.redirect_uri,
        }
        if code:
            data['code'] = code
        if refresh_token:
            data['refresh_token'] = refresh_token

        return await self.rest.request(Route('post', 'https://discordapp.com/api/v6/oauth2/token'), data=data)