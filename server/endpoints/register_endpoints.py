from endpoints.ping.ping import PING


def register(app):
    app.register_blueprint(PING)
