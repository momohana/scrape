import time
import re

import requests
import lxml.html
from pymongo import MongoClient

def main():
    # 複数のページをクロールするのでSessionを使う。
    session = requests.Session()
    response = session.get('http://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        time.sleep(1)
        response = session.get(url) # Sessionを使って詳細ページを取得する。
        ebook = scrape_detail_page(response)
        print(ebook)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    # 詳細ページのResponseから電子書籍の情報をdictで取得する。
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url':response.url,
        'title':root.cssselect('#bookTitle')[0].text_content(),
        'price':root.cssselect('.buy')[0].text_content(),
        'content':[h3.text_content() for h3 in root.cssselect('#content > h3')],
    }
    return ebook

def normalize_spaces(s):
    # 連続する空白を１つのスペースに置き換え、前後の空白は削除した新しい文字列を取得する。
    return re.sub(r'\s+','',s).strip()

if __name__ == '__main__':
    main()
