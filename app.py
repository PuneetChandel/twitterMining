from flask import Flask
from setup.config import config
from utils.database import Database
from api.api import api_route
app = Flask(__name__)
app.register_blueprint(api_route)
Database.initialize(config['dbName'])
app.run(host=config["flaskhost"], port=config["flaskport"])


