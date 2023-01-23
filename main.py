from flask import Flask
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
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


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return tasksJSON
