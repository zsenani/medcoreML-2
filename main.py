from flask import Flask, jsonify, request
import json
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return "App Works!!!"


@app.route('/search', methods = ['GET', 'POST'])
def tasks():
    if(request.method == 'POST'):
        request_data = request.data #getting the response data
        request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
        vector = request_data['vector'] #assigning it to name
        
        dt = joblib.load('finalized_model.sav')
        pca = joblib.load('pca.sav')
        vector = pca.transform([vector])
        predict = dt.predict(vector)
        #predict = dt.predict_proba(vector)
        return jsonify({'vector' : predict[0]})
    else: 
        return 'ELSE'
