from flask import Flask, jsonify
from flask_restful import Resource, Api
from azure.storage.blob import BlobServiceClient
import sys
import os
import json
from flask import request
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist, jaccard

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    dataset = pd.read_csv('https://github.com/zsenani/2022-GP-10/blob/37911ec695b28ee7b9d8d10e5e184d83190c98ea/MedCoreDataset.csv?raw=true')
    df = pd.DataFrame(dataset)
    df_new = df.iloc[:, 1:405]
    df_new.loc[len(df_new)] = [0,	0,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0,	0,	0,	1,	1,	0,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,  0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0]

    # Calculate similarity

    res = pdist(df_new, 'jaccard')
    squareform(res)
    distance =  1 - pd.DataFrame(squareform(res), index=df_new.index, columns= df_new.index)
    last_row_df = distance.iloc[-1:]
    last_row_json = last_row_df.to_json(orient ='records')
    jsondict = json.loads(last_row_json)
    first = list(jsondict)[0]
    s = pd.Series(first)
    rows = len(df.axes[0])

    arr = {}
    index = 0
    for i in s:
        if(i >= 0.3 and index != rows):
            arr[index] = i
        index +=1


    arr1 = {}
    for i in arr:
        aa = df.iloc[i:i+1, 0:1]
        aa = aa.to_json(orient ='values')
        jsondict = json.loads(aa)
        cc = list(jsondict)[0][0]
        arr1[cc] = arr[i]

    sorted_arr1 = sorted(arr1.items(), key=lambda x:x[1], reverse=True)
    return sorted_arr1
