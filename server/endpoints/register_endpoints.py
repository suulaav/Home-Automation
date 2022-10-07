from endpoints.ping.ping import register_ping
from endpoints.auth.auth import register_auth
from endpoints.bedroom.bedroom import register_bedroom


def register(app):
    register_ping(app)
    register_auth(app)
    register_bedroom(app)
