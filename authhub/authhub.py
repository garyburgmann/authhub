from config import authhub
from .factories.AuthHubFactory import AuthHubFactory


class AuthHub:

    # def __init__(self, request):
    #     self.request = request

    def driver(self, driver):
        ''' Returns an auth provider '''
        return AuthHubFactory(driver)
