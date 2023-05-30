from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, request
from googletrans import Translator
import pyodbc
import os
import json
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

class NewsClassifier(Resource):
    def post(self):
        
        translator = Translator()
        
        args = parser.parse_args()
        msg = args['data']
        msg = translator.translate(msg, dest='en').text
        #print(msg)
        prediction = model.predict([msg])
        
        return prediction.tolist()

import datetime
class NewsSaver(Resource):
    def post(self):
        
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()
        formatted_date = current_date.strftime("%Y-%m-%d")
        formatted_time = current_time.strftime("%H:%M:%S")
        data = json.loads(request.data)

        insert_user(data['name'], 'NULL' , data['email'])
        user_id = get_user_id(data['email'])

        cursor = conn.cursor()

        #query = '''
        #INSERT INTO dbo.News(TextNews, [Date], [Time], Label, OriginId, UserId)
        #VALUES (?, ?, ?, ?, ?, ?);
        #'''

        #cursor.execute(query, data['news'], current_date, formatted_time, float(data['label']), float(3), float(user_id)) 

        query = '''
        INSERT INTO dbo.News(TextNews, [Date], [Time], Label, OriginId, UserId)
        VALUES (?, ?, ?, ?, ?, ?);
        '''

        cursor.execute(query, data['news'], formatted_date, formatted_time, data['label'], 3, user_id)

        cursor.commit()

        return 'News data saved successfully. User id: ' + str(user_id)
    
def get_user_id(email):
    cursor = conn.cursor()

    query = '''
    SELECT UserId FROM dbo.Users WHERE Email = ?
    '''

    cursor.execute(query, email)

    return cursor.fetchone()[0]

def insert_user(name, surname, email):
    cursor = conn.cursor()

    query = '''
    IF NOT EXISTS (SELECT * FROM dbo.Users WHERE Email = ?)
    BEGIN
        INSERT INTO dbo.Users([Name],[Surname],[Email])
        VALUES (?, ?, ?);
    END
    '''

    cursor.execute(query, email, name, surname, email) 

    cursor.commit()

class UsersSaver(Resource):
    def post(self):

        data = json.loads(request.data)

        insert_user(data['name'], 'NULL' , data['email'])

        return get_user_id(data['email'])
    
# Define how the api will respond to the requests
api.add_resource(NewsClassifier, '/bert')
api.add_resource(NewsSaver, '/save-news')
api.add_resource(UsersSaver, '/save-user')

if __name__ == '__main__':

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    # Load model
    model = load_model()
    conn = pyodbc.connect('Driver={SQL Server};'
                'Server=DESKTOP-Q94UJ7E;'
                'Database=news;'
                'Trusted_Connection=yes;')

    app.run(debug=True)