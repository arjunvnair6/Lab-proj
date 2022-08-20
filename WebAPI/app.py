from flask import Flask,request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import pandas as pd

from ml import ML_Model

app = Flask(__name__)
api = Api(app)

class ML(Resource):
    
    def post(self):
        f = request.files['file']
        print(f)
        ml = ML_Model()
        data = ml.image_preprocessing(f)
        return data, 201

   
# Add URL endpoints
api.add_resource(ML, '/')
CORS(app, supports_credentials=True)
if __name__ == '__main__':
    app.run()