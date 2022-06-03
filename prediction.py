import pandas as pd
import pickle

def prediction(data):
    model = pickle.load('svm_model.pkl','rb')
    pred = model.predict(data)
    return pred