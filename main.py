from flask import Flask, jsonify, request
import json
import pickle as pk
import pandas as pd
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return "App Works!!!"


@app.route('/search', methods = ['GET', 'POST'])
def tasks():
    if(request.method == 'POST'):
        request_data = request.data #getting the response data
        request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
        vector = request_data['vector'] #assigning it to vector
        dataset = pd.read_csv('https://github.com/zsenani/medcoreML-2/blob/d9f5a98d70510682258f1e23bc3663c86a19455d/OO.csv?raw=true')
        df = pd.DataFrame(dataset)
        with open("dt_cv.pkl", 'rb') as dt:
            dt = pk.load(dt)
        predict = dt.predict([vector])
        
        #Get physID
        df_physID = df.query('prognosis == @predict[0]').iloc[:, 132:134]
        getPhys = df_physID.sample(n = 3)
        getPhys = getPhys.physID.drop_duplicates()
        
        #Symptoms pie chart
        df_Symptoms = df.query('prognosis == @predict[0]').iloc[:,0:132]
        symptoms = list(df_Symptoms.columns)
        symptoms_dic = dict()
        for i in symptoms:
            counts = Counter(df_Symptoms[i])
            if(counts[1] != 0):
                symptoms_dic[i] = counts[1]
        return jsonify({'vector' : predict[0], 'physID' : list(getPhys), 'symptomsDic' : symptoms_dic})
    else: 
        return 'ELSE'
