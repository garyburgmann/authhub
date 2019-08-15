from setuptools import setup

setup(
    name="authhub",
    version='0.0.32',
    packages=[
        'authhub',
        'authhub.commands',
        'authhub.drivers',
        'authhub.factories',
        'authhub.snippets',
    ],
    install_requires=[
        'masonite',
        'cleo',
        'requests'
    ],
    include_package_data=True,
)
