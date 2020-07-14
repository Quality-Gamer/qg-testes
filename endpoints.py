from service import GETRequest,POSTRequest,redisSetKey,redisGetKey,redisKeysKey
from keys import *

def indexEndpoint():
    return "Tests API - API from QualityGamer"

def testsEndpoint(user_id):
    data = POSTRequest('https://qg-usuario.herokuapp.com/api/tests/load',{'user_id':user_id})
    return data

def testsDoneEndpoint(user_id):
    data = POSTRequest('https://qg-usuario.herokuapp.com/api/tests/done',{'user_id':user_id})
    return data

def questionsEndpoint(user_id,match_id,order):
    data = POSTRequest('https://qg-usuario.herokuapp.com/api/tests/questions',{'user_id':user_id,'match_id':match_id})
    
    questions = data["response"]["questions"]
    question = selectQuestion(questions,order)

    return question

def saveAnswerEndpoint(match_id,order,user_id,option):
    data = POSTRequest('https://qg-usuario.herokuapp.com/api/tests/questions',{'user_id':user_id,'match_id':match_id})
    
    isValid = verifyOption(option)

    if not isValid:
        return {'status':'NOK', 'response': None, 'message': 'Essa opção de resposta não é válida'}

    questions = data["response"]["questions"]
    saveAnswer(user_id,match_id,order,option,questions)

    return {'status':'OK', 'response': None, 'message': 'Sucesso'}

def endTestEndpoint(match_id,user_id,test_id,win):
    keyPath = MICROSERVICE + ":" + TEST + ":" + str(user_id) + ":" + match_id + "*"
    keyCorrect = keyPath + ":" + CORRECT

    correctList = redisKeysKey(keyCorrect)
    score = getScore(correctList)
    response = saveUserTest(match_id,user_id,test_id,win,score)


    return response

def createTestEndpoint(match_id,user_id,test_id,win):
    data = POSTRequest('https://qg-usuario.herokuapp.com/api/tests/save',{'user_id':user_id,'test_id':test_id})
    return data

def saveUserTest(match_id,user_id,test_id,win,score):
    data = POSTRequest('https://qg-usuario.herokuapp.com/api/tests/save',{'user_id':user_id,'match_id':match_id,'win':win,'score':score,'test_id':test_id})
    return data

def getScore(corrects):
    l = len(corrects)
    if(l == 0):
        return 0

    correctsAnswers = 0

    for key in corrects:
        correctsAnswers = correctsAnswers + int(redisGetKey(key))

    return int(correctsAnswers/l)

def selectQuestion(questions,order,hide = True):
    for question in questions:
        if int(question["order"]) == int(order):
            if(hide):
                question["response"] = "??"
            return question

    return {'status':'NOK', 'response': None, 'message': 'Essa pergunta não existe'}

def saveAnswer(user_id,match_id,order,option,questions):
    question = selectQuestion(questions,order,False)
    keyPath = MICROSERVICE + ":" + TEST + ":" + str(user_id) + ":" + match_id + ":" + str(question['id'])
    keyAnswer = keyPath + ":" + ANSWER
    keyCA = keyPath + ":" + CORRECT_ANSWER
    keyCorrect = keyPath + ":" + CORRECT
    correctAnswer = 0

    if str(option) == str(question['response']):
        correctAnswer = 1
    
    redisSetKey(keyAnswer,option)
    redisSetKey(keyCA,question['response'])
    redisSetKey(keyCorrect,correctAnswer)


def verifyOption(option):
    return True if (option == 'A' or option == 'B' or option == 'C' or option == 'D' or option == 'X') else False

