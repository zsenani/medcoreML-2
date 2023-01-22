from flask import Flask, jsonify
from flask_restful import Resource, Api
from azure.storage.blob import BlobServiceClient
import sys
import os
import json
from flask import request
import pandas as pd
#from flask import Flask, jsonify
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist, jaccard

app = Flask(__name__)
api = Api(app)
# prot = 5000
# storage_account_key='wsKVsviqBS6WZnM61CMWjwEPRmX4U5AK3uod/HJY+EOj7VMgGbHldJTf4DGBjnms4v8XDSq1wcbb+AStRmtgrw=='
# storage_account_name='medcorestorage'
# connection_string='DefaultEndpointsProtocol=https;AccountName=medcorestorage;AccountKey=ztfiERoaOezdZLc84vyJAl0darwqKW94e8spih+R2/VJrltdwoPJj5ghZliifTZuUqTJ1/qmE2i2+ASthzevdA==;EndpointSuffix=core.windows.net'
# container_name='file-holder'
# def uploadToBlobStorage(file_path,file_name):
#    blob_service_client = BlobServiceClient.from_connection_string(connection_string) 
#    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name) 
#    with open(file_path,'rb') as data:      
#         blob_client.upload_blob(data)     
#    print(f"Uploaded {file_name}.")
#    # calling a function to perform upload

# uploadToBlobStorage('dataset.csv','dataset.csv')

class helloworld(Resource):
    def post(self):
        print('a')
        vector=request.get_json()["name"]
        print('bb')
        dataset= pd.read_csv('https://github.com/zsenani/2022-GP-10/blob/37911ec695b28ee7b9d8d10e5e184d83190c98ea/MedCoreDataset.csv?raw=true')
        print(dataset)
        df = pd.DataFrame(dataset)
        df_new = df.iloc[:, 1:405]
        df_new.loc[len(df_new)] = vector
#[0,    0,  0,  0,  0,  1,  0,  1,  0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0, 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0   ,0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0   ,0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0]    
        res = pdist(df_new, 'jaccard')
        squareform(res)
        distance = 1 - pd.DataFrame(squareform(res), index=df_new.index, columns= df_new.index)
        last_row_df = distance.iloc[-1:]
        last_row_json = last_row_df.to_json(orient ='records')
        jsondict = json.loads(last_row_json)
        first = list(jsondict)[0]
        s = pd.Series(first)
        rows = len(df.axes[0])
        print(distance)
        arr = {}

        index = 0
        for i in s:
            if(i >= 0.01 and index != rows):
                arr[index] = i
                #print(index,"-",i)
            index +=1
        # arr1 = pd.Series(arr)
        # arr1 = arr1.nlargest()
        arr1 ={}
    
        for i in arr:
            aa = df.iloc[i:i+1, 0:1]
            aa = aa.to_json(orient ='values')
            jsondict = json.loads(aa)
            cc = list(jsondict)[0][0]
            arr1[cc] = arr[i]
        sorted_arr1 = sorted(arr1.items(), key=lambda x:x[1], reverse=True)
        print(sorted_arr1)
    
#last_row_df = distance.iloc[-1:].idxmin(axis=1)
# distance.to_csv('distance.csv')
        return sorted_arr1

api.add_resource(helloworld,'/')

# @app.route('/', methods=['GET'])
# def index():   
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0")
   
