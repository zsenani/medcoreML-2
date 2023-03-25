from flask import Flask, jsonify, request
import json
import pickle as pk
import pandas as pd
#from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return "App Works!!!"


@app.route('/search', methods = ['GET', 'POST'])
def tasks():
    if(request.method == 'POST'):
        dataset = pd.read_csv('https://github.com/zsenani/medcoreML-2/blob/d9f5a98d70510682258f1e23bc3663c86a19455d/OO.csv?raw=true')
#         request_data = request.data #getting the response data
#         request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
#         vector = request_data['vector'] #assigning it to vector
        vector = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0]
        with open("pca.pkl", 'rb') as pca:
            pca = pk.load(pca)
        with open("dt.pkl", 'rb') as dt:
            dt = pk.load(dt)
        vector = pca.transform([vector])
        predict = dt.predict(vector)
        
        #Get physID
        df_physID = df.query('prognosis == @predict[0]').iloc[:, 132:134]
        getPhys = df_physID.sample(n = 3)
        getPhys = getPhys.physID.drop_duplicates()
        
#         #Symptoms pie chart
#         df_Symptoms = df.query('prognosis == @predict[0]').iloc[:,0:132]
#         symptoms = list(df_Symptoms.columns)
#         symptoms_dic = dict()
#         for i in symptoms:
#             counts = Counter(df_Symptoms[i])
#             if(counts[1] != 0):
#                 symptoms_dic[i] = counts[1]
        return jsonify({'vector' : predict[0], 'physID' : list(getPhys)})
    else: 
        return 'ELSE'
