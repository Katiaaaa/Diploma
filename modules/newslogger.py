from flask_restful import Resource

class NewsLogger(Resource):
    def put(self):
        
        args = parser.parse_args()

        return args