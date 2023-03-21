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
        vector = [1,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0,	0,	0,	0,	1,	1,	0,	1,	0,	0,1,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,	0,	0,	0,	0,	1,	0,	1,	0,	0,0,0]
        dt = joblib.load('https://github.com/zsenani/medcoreML-2/blob/bd6b027876bd1b0de0e25b728cf77dbaad9e40eb/finalized_model.sav')
        pca = joblib.load('https://github.com/zsenani/medcoreML-2/blob/bd8598aafc9e1bd48daa186902008fc9b37d9e04/pca.sav')
        vector = pca.transform([vector])
        predict = dt.predict(vector)
        #predict = dt.predict_proba(vector)
        return jsonify({'vector' : predict[0]})
    else: 
        return 'ELSE'
