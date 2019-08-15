""" An AuthHub Factory for driver selection """
from authhub.drivers import (
    GitHubDriver,
    GoogleDriver
)


class AuthHubFactory:

    @staticmethod
    def driver(driver_name):
        if driver_name == 'google':
            return GoogleDriver()
        if driver_name == 'github':
            return GitHubDriver()
        raise NotImplementedError('Factory not found')
