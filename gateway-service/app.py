from flask import Flask, request, jsonify
import requests

app = Flask(name)

GREETING_URL = 'http://greeting-service:5000/greeting'
SUM_URL = 'http://sum-service:5001/sum'

@app.route('/greeting', methods=['GET'])
def greeting_proxy():
    response = requests.get(GREETING_URL, params=request.args)
    return response.text, response.status_code

@app.route('/sum', methods=['GET'])
def sum_proxy():
    response = requests.get(SUM_URL, params=request.args)
    return response.text, response.status_code

if name == 'main':
    app.run(host='0.0.0.0', port=8080)
