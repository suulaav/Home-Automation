from endpoints import register_endpoints
from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = "TEST@123"
register_endpoints.register(app)


@app.route('/')
def root():
    return "Lost ?"


# Socket IO

# @socketio.on('lights')
# @token_required
# def lights(current_user, data):
#     Light_1 = data["Light 1"]
#     Light_2 = data["Light 2"]
#     emit('response', {"Light 1 is ": Light_1, "Light 2 is ": Light_2}, broadcast=True)


if __name__ == "__main__":
    # set_app(app)
    # app.run(debug=True)
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
