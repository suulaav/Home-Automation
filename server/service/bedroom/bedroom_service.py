from database import changes
from helper.response.rest_response import Response
from service.bedroom.BedroomInterface import BedroomInterface


class BedroomService(BedroomInterface):

    def __init__(self, app):
        self.app = app

    def get_data(self):
        is_valid = 0
        _id = None
        while not is_valid:
            change = changes.get_data_changes()
            if change:
                change = [dict(row) for row in change][0]
                is_valid = change['is_valid']
                _id = change['id']
        changes.set_executed_flag(_id)
        return Response.ok(change['data'])

    def set_data(self, user, request):
        order = request.json
        post = order['data']
        request_id = changes.register_request(user, post)
        return Response.ok({"id": request_id})
