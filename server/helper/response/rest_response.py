import datetime



class Response:
    @staticmethod
    def ok(data=None):
        okResponse = dict()
        okResponse['code'] = 0
        okResponse['data'] = data
        okResponse['time'] = datetime.datetime.now()
        return okResponse
