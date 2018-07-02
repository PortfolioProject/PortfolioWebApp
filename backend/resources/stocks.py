from flask_restful import Resource

class Stock(Resource):
    def get(self):
        return {'Hello': 'World'}

