from endpoints import register_endpoints
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "TEST@123"
register_endpoints.register(app)


@app.route('/')
def root():
    return "Lost ?"


if __name__ == "__main__":
    app.run(debug=True)
