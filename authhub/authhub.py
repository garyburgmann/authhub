from config import services
from pydoc import locate

class AuthHub(object):

    def __init__(self, request):
        self.request = request

    def driver(self, driver):
        ''' Returns an auth provider '''
        processor = services.AUTH_PROVIDERS[driver]
        return locate(processor['driver'])(self.request, processor)
