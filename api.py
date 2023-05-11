from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from googletrans import Translator
import os



from model import load_model

app = Flask(__name__)
api = Api(app)


@app.after_request
def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')

# Define how the api will respond to the post requests
class NewsClassifier(Resource):
    def post(self):
        
        translator = Translator()
        
        args = parser.parse_args()
        msg = args['data']
        msg = translator.translate(msg, dest='en').text
        #print(msg)
        prediction = model.predict([msg])
        
        return prediction.tolist()

api.add_resource(NewsClassifier, '/bert')

if __name__ == '__main__':

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    # Load model
    model = load_model()
    app.run(debug=True)