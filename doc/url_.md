# URLの基礎知識
クローラーでリンクをたどるには、リンクを表す`a`タグの`href`属性から次のページのURLを取得します。このとき得られたURLが相対URLだった場合は、絶対URLに変換する必要があります。URLの構造、絶対URLと相対URLの違い、Pythonでの相対URLから絶対URLへの変換を解説します。

## URLの構造
**URL**は`Unform ResourceLocator`の略で、インターネット上に存在するリソース(ファイルなど)の場所を表す識別子です。

表1 URLの各部分の意味

|URLの部分|説明|
|:--|:--|
|スキーム|`http`や`https`のように**プロトコル**を表す。|
|オーソリティ|`//`の後に続き、通常**ホスト名**を表す。 ユーザー名やパスワード、ポート番号を含む場合もある。|
|パス|`/`で始まり、そのホストにおけるリソースの**パス**を表す。|
|クエリ|`?`の後に続き、パスとは異なる方法でリソースを指定するために使われる。|
|フラグメント|`#`のあとに続き、リソース内の特定の部分を表す。|

## 絶対URLと相対URL
URLには大きく分けて絶対URLと相対URLがあります。これらの言葉には明確な定義がなく、人によってマチマチです。本書では、`http://`などのスキームで始まるURLを**絶対URL**と定義します。それ以外の、基準となる絶対URLがあり、それに対する相対的なURLを表すものを**相対URL**と定義します。相対URLには3種類の形式があります。

1. `//`で始まる相対URL
2. `/`で始まる相対URL
3. それ以外の相対パス形式の相対URL

例を表2に示します。基準となる絶対URLは、`http://example.com/books/top.html`です。

表2 相対URLの例

|形式|相対URL|相対URLが指す絶対URL|
|--:|:--|:--|
|1|//cdn.example.com/logo.png|http://cdn.example.com/logo.png|
|2|/articles/|http://example.com/articles/|
|3|./|http://example.com/books/|

## 相対URLから絶対URLへの変換
Pythonで相対URLを絶対URLに変換するには、標準ライブラリの`urllib.parse`モジュールに含まれる`urljoin()`関数を使います。`urljoin()`関数は、第1引数に基準となるURLを指定し、第2引数に相対URLを指定します。

```python
>>> from urllib.parse import urljoin
>>> base_url = 'http://example.com/books/top.html'
>>> urljoin(base_url, '//cdn.example.com/logo.png') # //で始まる相対URL
'http://cdn.example.com/logo.png'
>>> urljoin(base_url, '/articles') # /で始まる相対URL
'http://example.com/articles/'
```
