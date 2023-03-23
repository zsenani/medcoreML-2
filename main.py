from flask import Flask, jsonify, request
import json
import pickle as pk

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
        with open("pca.pkl", 'rb') as pca:
            pca = pk.load(pca)
        with open("dt.pkl", 'rb') as dt:
            dt = pk.load(dt)
        vector = pca.transform([vector])
        predict = dt.predict(vector)
        return jsonify({'vector' : predict[0]})
    else: 
        return 'ELSE'
