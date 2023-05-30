from flask_restful import Resource
from googletrans import Translator

class NewsClassifier(Resource):
    def post(self):
        
        translator = Translator()
        
        args = parser.parse_args()
        msg = args['data']
        msg = translator.translate(msg, dest='en').text
        #print(msg)
        prediction = model.predict([msg])
        
        return prediction.tolist()