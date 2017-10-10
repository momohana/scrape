import lxml.html
from pymongo import MongoClient

# HTMLファイルを読み込み、getroot()メソッドでHtmlElementオブジェクトを得る。
tree = lxml.html.parse('index.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)
db = client.scraping
collection = db.links

collection.delete_many({})

# cssseselect()メソッドでa要素のリストを取得して、個々のa要素に対して処理を行う。
for a in html.cssselect('a'):
    # href属性とリンクのテキストを取得して保存する。
    collection.insert_one({
        'url':a.get('href'),
        'title':a.text
    })

# コレクションのすべてのドキュメントを_idの順にソートして取得する。
for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])
