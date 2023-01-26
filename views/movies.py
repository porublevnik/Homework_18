from flask_restx import Resource, Namespace

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
