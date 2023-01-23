from flask import Flask
from flask import Flask, jsonify
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist, jaccard
import json

app = Flask(__name__)

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

tasks = [
    {
        'id': index,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        "id": 2,
        "name": "task2",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "task3",
        "description": "This is task 3"
    }
]

tasksJSON = json.dumps(tasks)
#tasksJSON = jsonify({'name' : sorted_arr1})

@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return tasksJSON
