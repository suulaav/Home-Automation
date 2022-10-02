import datetime


class Response:
    @staticmethod
    def ok(data):
        okResponse = dict()
        okResponse['code'] = 200
        okResponse['data'] = data
        okResponse['time'] = datetime.datetime.now()
        return okResponse
