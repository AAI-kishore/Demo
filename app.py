from crypt import methods
from flask import Flask
from sklearn import datasets
from prediction import get_prediction

import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def xyz():
    return ''' Welcome to world of possibilities of Flask Application'''

def score():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
        logging.info(f"""{data}""")
        
    try:
        scoring_data= main_likelyhood_model(dealID)
        except:
            return "error in predicting from the model"

    model=pickle.load('svm_model.pkl','rb')
    model.predict()