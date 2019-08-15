""" Masonite AutHub Settings """
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

AUTH_PROVIDERS = {
    'google': {
        'client': os.environ.get('GOOGLE_CLIENT'),
        'secret': os.environ.get('GOOGLE_SECRET'),
        'redirect': os.environ.get('GOOGLE_REDIRECT'),
        'scopes': ['profile', 'email']
    },
    'github': {
        'client': os.environ.get('GITHUB_CLIENT'),
        'secret': os.environ.get('GITHUB_SECRET'),
        'redirect': os.environ.get('GITHUB_REDIRECT'),
        'scopes': ['read:user', 'public_repo']
    }
}
