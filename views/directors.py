from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
