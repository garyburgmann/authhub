""" The GitHub AuthHub Driver """
from config import authub
import requests
import json
try:
    from config import authub as app_config
    github_config = app_config.AUTH_PROVIDERS['github']
except ImportError:
    raise ImportError('Config not found for GitHub')

class GitHubDriver(object):

    def __init__(self):
        self.scopes = None
        self._config = github_config

    def redirect(self):
        """ Redirect to GitHub """
        if self.scopes:
            scopes = ' '.join(self.scopes)
        else:
            scopes = ''

        return self.request.redirect('https://github.com/login/oauth/authorize?client_id={0}&scope={1}&state={2}&redirect_uri={3}'.format(self.processor['client'], scopes, self._state, self.processor['redirect']))

    def scope(self, *args):
        ''' Set Scopes '''
        self.scopes = args
        return self

    def state(self, state):
        ''' Set State '''
        self._state = state
        return self

    def user(self):
        ''' Get the user from the oAuth flow '''

        payload = {
            'client_id': self.processor['client'],
            'client_secret': self.processor['secret'],
            'code': self.request.input('code')
        }

        # Request an access token from the code in the request
        response = requests.post('https://github.com/login/oauth/access_token', params=payload)

        # Get the access token from the response
        access_token = response.text

        # Exchange the access token for a user
        user = requests.get('https://api.github.com/user?{0}'.format(access_token))
        return json.loads(user.text)
