""" The GitHub AuthHub Driver """
import json
import urllib

import requests
from masonite.response import Response

try:
    from config import authub as app_config
    print('app_config: ', app_config)
    print('app_config.AUTH_PROVIDERS: ', app_config.AUTH_PROVIDERS)
    provider_config = app_config.AUTH_PROVIDERS['google']
except ImportError:
    raise ImportError('Config not found for Google')


class GoogleDriver:
    access_token_url = 'https://accounts.google.com/o/oauth2/token'
    authorization_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    profile_url = 'https://www.googleapis.com/oauth2/v3/userinfo'

    def __init__(self):
        self.scopes = provider_config['scopes']
        self._config = provider_config

    def redirect(self, response: Response):
        """ Redirect to Google """
        if self.scopes:
            scopes = ' '.join(self.scopes)
        else:
            scopes = ''

        params = dict(
            scope=scopes,
            access_type='offline',
            redirect_uri=self._config['redirect'],
            response_type='code',
            client_id=self._config['client']
        )
        
        endpoint = f'{self.authorization_url}?{urllib.parse.urlencode(params)}'
        return response.redirect(endpoint)

    def scopes(self, *args):
        ''' Set Scopes '''
        self.scopes = args
        return self

    # def state(self, state):
    #     ''' Set State '''
    #     self._state = state
    #     return self

    # def user(self):
    #     ''' Get the user from the oAuth flow '''

    #     payload = {
    #         'client_id': self.processor['client'],
    #         'client_secret': self.processor['secret'],
    #         'code': self.request.input('code')
    #     }

    #     # Request an access token from the code in the request
    #     response = requests.post('https://github.com/login/oauth/access_token', params=payload)

    #     # Get the access token from the response
    #     access_token = response.text

    #     # Exchange the access token for a user
    #     user = requests.get('https://api.github.com/user?{0}'.format(access_token))
    #     return json.loads(user.text)
