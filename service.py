import requests
import redis
import json
import os

def GETRequest(url):
    r = requests.get(url = url) 
        
    data = r.json() 
    return data
        

def POSTRequest(url,params):
    r = requests.post(url, data = params)
        
    data = r.json() 
    return data

def redisConn():
    return redis.Redis.from_url(os.getenv('REDISCLOUD_URL'))

def redisGetKey(key):
    r = redisConn()
    return r.get(key)

def redisSetKey(key,value):
    r = redisConn()
    r.set(key,value)

def redisKeysKey(key):
    r = redisConn()
    listKeys = r.keys(key)
    s = []
    for x in listKeys: s.append(x.decode("utf-8"))
    
    return s