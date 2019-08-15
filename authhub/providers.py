""" An AuthHub Service Provider """
from masonite.provider import ServiceProvider
from authhub.commands.InstallCommand import InstallCommand
from authhub.authhub import AuthHub


class AuthProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('AuthHubInstallCommand', InstallCommand())
        self.app.bind('AuthHub', AuthHub)

    def boot(self):
        pass
