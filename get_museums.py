from SPARQLWrapper import SPARQLWrapper


# SPARQLエンドポイントのURLを指定してインスタンスを作成する。
sparql = SPARQLWrapper('http://ja.dbpedia.org/sparql')

# 日本の美術館を取得するクエリを設定する。バックスラッシュを含むのでrで始まるraw文字列を使用している。
sparql.setQuery(r'''
    SELECT * WHERE {
        ?s rdf:type dbpedia-owl:Museum ;
          prop-ja:所在地 ?address .
          OPTIONAL { ?s rdfs:label ?label .}
          OPTIONAL {
          ?s prop-ja:軽度度 ?lon_degree ;
             prop-ja:軽度分 ?lon_minute ;
             prop-ja:軽度病 ?lon_second ;
             prop-ja:緯度度 ?lat_degree ;
             prop-ja:緯度分 ?lat_minute ;
             prop-ja:緯度秒 ?lat_second .
          }
        FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
    } ORDER BY ?s
''')

# 取得するフォーマットとしてJSONを指定する。
sparql.setReturnFormat('json')

# query()でクエリを実行し、convert()でレスポンスをパースしてdictを得る。
response = sparql.query().convert()

# 抽出した変数の値を表示する。
for result in response['results']['bindings']:
    print(result['s']['value'], result['address']['value'])
