from django.conf import settings
import random

def global_vars(request):
    return {
        'links': [
            {'title': 'Home', 'url': '/ex'}
        ]
    }

def global_sessions(request):
    request.session.clear_expired()
    if request.session.has_key('auth'):
        username = 'Araiva'
    else:
        username = set_anonymous(request)
    return {
        'session': {
            'username': username
        }
    }

def set_anonymous(request):
    request.session.clear_expired()
    request.session.set_expiry(42)
    username = request.session.get('username')
    if not username:
        selected = random.choices(settings.USERNAMES)
        username = selected[0]
        request.session['username'] = username
    return username