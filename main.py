from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    sum = 1 + 1
    return jsonify({'sum' : sum})
