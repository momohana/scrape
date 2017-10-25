from robobrowser import RoboBrowser

# RoboBrowserオブジェクトを作成する。キーワード引数parserはBeautifulSoup()の第2引数として使われる。
browser = RoboBrowser(parser='html.parser')

browser.open('https://www.google.co.jp')

# 検索語を入力して送信する。
form = browser.get_form(action='/search')
# フォームのqという名前のフィールドに検索語を入力。
form['q'] = 'Python'
# 1つめのボタン(Google検索)を押す。
browser.submit_form(form, list(form.submit_fields.value())[0])

# 検索結果のタイトルとURLを抽出して表示する。
# select()メソッドはBeautifulSoupのselect()メソッドと同じものであり、引数のCSSセレクタにマッチする要素に対応するTagオブジェクトのリストを取得できる。
for a in browser.select('h3 > a'):
    print(a.text)
    print(a.get('href'))
