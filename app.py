import pandas as pd
from flask import Flask, request
from sklearn import datasets
import json
import pickle

app = Flask(__name__)

@app.route('/')

def xyz():
    return ''' Welcome to world of possibilities of Flask Application'''

# def score():
#     # content_type = request.headers.get('Content-Type')
#     # if (content_type == 'application/json'):
#     #     data = json.loads(request.data)
#     #     logging.info(f"""{data}""")
#     #     print(data)

#     data = pd.Series([1.76,2.87,2.7,2.4],index=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] )
#     print(data)
#     with open('svm_model.pkl','rb') as f:
#         model = pickle.load(f)
#     pred = model.predict(data)
#     return pred
