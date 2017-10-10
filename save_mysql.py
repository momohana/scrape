import mysql.connector

# MySQLサーバーに接続し、コネクションを取得する。
connect = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'scraper',
    password = 'take1215',
    database = 'scraping',
    charset = 'utf8')

# カーソルを取得する。
cursor = connect.cursor()

# SQL文を実行する（このスクリプトを何回実行しても同じ結果になるように、citiesテーブルが存在する場合は削除する。
cursor.execute('DROP TABLE IF EXISTS cities')

# citiesテーブルを作成する。
cursor.execute('''
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
''')

# パラメーターで置き換える場所は、%sで指定する
cursor.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, '上海', 24150000))

# パラメーターが辞書の場合、プレースホルダーは%(名前)sで指定する。
cursor.execute('INSERT INTO cities VALUE (%(rank)s, %(city)s, %(population)s)', {'rank':2, 'city':'カラチ', 'population':23500000})

# executemany()メソッドでは、複数のパラメーターをリストで指定し、複数のSQL文を実行する。
cursor.executemany('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)', [
    {'rank':3, 'city':'北京', 'population':21516000},
    {'rank':4, 'city':'天津', 'population':14722100},
    {'rank':5, 'city':'イスタンブール', 'population':14160467}
])

# 変更をコミットする。=
connect.commit()

# 保存したデータを取得する。
cursor.execute('SELECT * FROM cities')

# クエリの結果をfetchall()メソッドで取得する。
for row in cursor.fetchall():
    print(row)

# コネクションを閉じる
connect.close()
