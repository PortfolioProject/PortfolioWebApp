from flask import Flask
from flask_restful import Api
from .resources.stocks import Stock

app = Flask(__name__)
api = Api(app)

api.add_resource(Stock, '/stock')
