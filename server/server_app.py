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



if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
