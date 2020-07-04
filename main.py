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

@app.route("/tests")
def tests():
    email = str(request.args.get('email'))
    password = str(request.args.get('password'))

    return jsonify(testsEndpoint(email,password))

@app.route("/done")
def done():
    email = str(request.args.get('email'))
    password = str(request.args.get('password'))

    return jsonify(testsDoneEndpoint(email,password))

@app.route("/questions")
def questions():
    email = str(request.args.get('email'))
    password = str(request.args.get('password'))
    match_id = str(request.args.get('match_id'))
    order = str(request.args.get('order'))

    return jsonify(questionsEndpoint(email,password,match_id,order))

@app.route("/save")
def save():
    email = str(request.args.get('email'))
    password = str(request.args.get('password'))
    match_id = str(request.args.get('match_id'))
    order = str(request.args.get('order'))
    user_id = int(request.args.get('user_id'))
    option = str(request.args.get('option'))

    return jsonify(saveAnswerEndpoint(email,password,match_id,order,user_id,option))

@app.route("/end")
def end():
    email = str(request.args.get('email'))
    password = str(request.args.get('password'))
    match_id = str(request.args.get('match_id'))
    user_id = int(request.args.get('user_id'))
    test_id = str(request.args.get('test_id'))
    win = str(request.args.get('win'))

    return jsonify(endTestEndpoint(email,password,match_id,user_id,test_id,win))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)