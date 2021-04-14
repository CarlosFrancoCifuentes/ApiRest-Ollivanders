from flask_restful import Resource

class WelcomeOllivanders(Resource):
    def get(self):
        return {'hello': 'Ollivanders'}