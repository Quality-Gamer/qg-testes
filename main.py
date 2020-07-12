from flask import Flask,jsonify,request
from flask_cors import CORS
import os
from endpoints import testsEndpoint,indexEndpoint,testsDoneEndpoint,questionsEndpoint,saveAnswerEndpoint,endTestEndpoint

app = Flask(__name__)
cors = CORS(app)
port = os.getenv('PORT') if os.getenv('PORT') else "8008"

@app.route("/")
def main():
    return jsonify(indexEndpoint())

@app.route("/api/tests",methods=['POST'])
def tests():
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))

    return jsonify(testsEndpoint(email,password))

@app.route("/api/done",methods=['POST'])
def done():
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))

    return jsonify(testsDoneEndpoint(email,password))

@app.route("/api/questions",methods=['POST'])
def questions():
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))
    match_id = str(request.form.get('match_id'))
    order = str(request.form.get('order'))

    return jsonify(questionsEndpoint(email,password,match_id,order))

@app.route("/api/save",methods=['POST'])
def save():
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))
    match_id = str(request.form.get('match_id'))
    order = str(request.form.get('order'))
    user_id = int(request.form.get('user_id'))
    option = str(request.form.get('option'))

    return jsonify(saveAnswerEndpoint(email,password,match_id,order,user_id,option))

@app.route("/api/end",methods=['POST'])
def end():
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))
    match_id = str(request.form.get('match_id'))
    user_id = int(request.form.get('user_id'))
    test_id = int(request.form.get('test_id'))
    win = int(request.form.get('win'))

    return jsonify(endTestEndpoint(email,password,match_id,user_id,test_id,win))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)