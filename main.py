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

@app.route("/api/tests")
def tests():
    user_id = str(request.args.get('user_id'))

    return jsonify(testsEndpoint(user_id))

@app.route("/api/done")
def done():
    user_id = str(request.args.get('user_id'))

    return jsonify(testsDoneEndpoint(user_id))

@app.route("/api/questions")
def questions():
    user_id = str(request.args.get('user_id'))
    match_id = str(request.args.get('match_id'))
    order = str(request.args.get('order'))

    return jsonify(questionsEndpoint(user_id,match_id,order))

@app.route("/api/save")
def save():
    match_id = str(request.args.get('match_id'))
    order = str(request.args.get('order'))
    user_id = int(request.args.get('user_id'))
    option = str(request.args.get('option'))

    return jsonify(saveAnswerEndpoint(match_id,order,user_id,option))

@app.route("/api/send")
def end():
    match_id = str(request.args.get('match_id'))
    user_id = int(request.args.get('user_id'))
    test_id = int(request.args.get('test_id'))
    win = int(request.args.get('win'))

    return jsonify(endTestEndpoint(match_id,user_id,test_id,win))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)