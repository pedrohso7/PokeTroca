from flask import Flask
from flask_cors import CORS
from src.main.routes.api_route import api_routes_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_routes_bp)

app.run(host="0.0.0.0", port=5000)