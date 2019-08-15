""" An AuthHub Service Provider """
from masonite.provider import ServiceProvider
from authhub.commands.InstallCommand import InstallCommand


class AuthProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('AuthHubInstallCommand', InstallCommand())

    def boot(self):
        pass
