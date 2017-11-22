from flask import Flask, Blueprint
from app      import api
from database import db
from app.products.ressources import ns as ns_product
import config

app = Flask(__name__)

app.config['SERVER_NAME'] = config.FLASK_SERVER_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS


blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(ns_product)
app.register_blueprint(blueprint)

db.init_app(app)

if __name__ == '__main__':
	app.run(debug=config.FLASK_DEBUG)