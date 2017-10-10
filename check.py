import requests

response = requests.get("https://gihyo.jp/dp")
response.status_code
response.headers
response.text
r = requests.get('https://gihyo.jp/dp')
type(r)
r.status_code
r.headers['content-type']
r.encoding
r.text
r = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010")
r.json()

# POSTメソッドで送信。キーワード引数data
r = requests.post('http://httpbin.org/post', data={'key1':'value1'})
r.content

import lxml.html
import os
tree = lxml.html.parse('index.html')

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.spots

# find()メソッドですべてのドキュメントを取得するためのCursorオブジェクトを取得することができる。
collection.find()

for spot in collection.find():
    print(spot)
    
