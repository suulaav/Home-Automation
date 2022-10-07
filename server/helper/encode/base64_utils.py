import base64


def encode(message):
    return base64.b64encode(message.encode('ascii'))
