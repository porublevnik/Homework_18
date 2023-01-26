from flask_restx import Resource, Namespace

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
