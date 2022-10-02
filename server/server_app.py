from endpoints import register_endpoints
from flask import Flask

app = Flask(__name__)
register_endpoints.register(app)

if __name__ == "__main__":
    app.run(debug=True)
