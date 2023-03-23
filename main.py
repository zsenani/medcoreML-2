from flask import Flask, jsonify, request
import json
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return "App Works!!!"


@app.route('/search', methods = ['GET', 'POST'])
def tasks():
    if(request.method == 'GET'):
        #request_data = request.data #getting the response data
        #request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
        #vector = request_data['vector'] #assigning it to name
        vector = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0]
        pca_reload = pk.load(open("pca.pkl",'rb'))
        dt_reload = pk.load(open("dt.pkl",'rb'))
        vector = pca_reload.transform([vector])
        predict = dt_reload.predict(vector)
        #predict = dt.predict_proba(vector)
        return jsonify({'vector' : predict[0]})
    else: 
        return 'ELSE'
