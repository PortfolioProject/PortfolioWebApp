from flask import Flask
from flask_restful import Api
from backend.resources.stocks import Stock
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

api.add_resource(Stock, '/stock')
