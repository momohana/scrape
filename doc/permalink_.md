# パーマリンクとリンク構造のパターン
パーマリンクとwebサイトのリンク構造を理解するとクローラーの開発が容易になります。パーマリンクのの概要と、本書が独自にまとめたリンク構造の理解に役立つパターンを解説します。

## パーマリンク
今日の多くのwebサイトでは、１つのコンテンツが対応する１つのURLを持ちます。例えば、技術評論社の電子書籍販売サイトでは、「Pythonエンジニア養成読本」という１つの電子書籍が次のURLに対応します。

`https://gihyo.jp/dp/ebook/2015/978-4-7741-7362-7`

このように、１つのコンテンツに対応し、時間が経っても対応するコンテンツが変わらないURLを**パーマリンク(Permalink)**と呼びます。「不変の」という意味の英単語`permanent`と`link`を組み合わせた言葉です。

パーマリンクを持つwebサイトは、Googleなどの検索エンジンのクローラーがコンテンツを認識しやすく、SEO(検索エンジン最適化)に強くなります。

## 一覧・詳細パターン
パーマリンクを利用するwebサイトでは、多くの場合、パーマリンクを持つページへのリンクが一覧となっているページが存在します。例えば、技術評論社の電子書籍販売サイトでは、次のURLが表すページに新着電子書籍の一覧が表示され、個別の電子書籍へのリンクが張られています。

`https://gihyo.jp/dp`

このサイトのリンク構造をまとめると次のようになります。

- 一覧ページ：電子書籍の一覧が表示され、詳細ページへのリンクが張られている。
- 詳細ページ：電子書籍の詳細な情報が表示されている。

このような一覧ページと詳細ページの組み合わせで構成されているwebサイトのリンク構造パターンを、本書では**一覧・詳細パターン**と呼ぶことにします。

表1 パーマリンクに含まれる一意な識別子の例

|コンテンツ|パーマリンクの例(強調部分が識別子)|識別子の意味|
|:--|:--|:--|
|Yahoo!ファイナンスの株価情報|http://stocks.finance.yahoo.co.jp/stocks/detail/?code=`8411`|証券コード|
|Amazonの商品情報|http://www.amazon.co.jp/dp/`B00CTTL5XQ`|ASIN|
|Twitterのツイート|https://twitter.com/TwitterJP/status/`606602260307509248`|ツイートID|
|ITmediaのニュースの記事|http://www.itmedia.co.jp/news/articles/`1506/08/news123`.html|年月日と番号|

## データを一意に識別するキー
パーマリンクに使われている識別子の意味を考えるのも効果的です。表の例では、Yahoo!ファイナンスの`8411`という値は証券コードと呼ばれる日本の証券取引所に上場している企業に付与されているコードです。

## データベースの設計
データを一意に識別するキーが決まったら、このキーを格納するフィールドにデータベースのユニーク制約を設定することで、データの一意性を保証できます。

データベースの主キーには、このキーとは別にサロゲートキーと呼ばれるデータベース側で自動生成されるキーを使うのがおすすめです。webページのURLとそこから取得可能な識別子は、webサイト側のリニューアルなどで変わる可能性があるためです。サロゲートキーを使っていれば影響が少なくて済みます。

サロゲートキーの例としては次のようなものがあります。MySQLでは列に`AUTO_INCREMENT`という属性を設定すると、自動的に連番が振られます。MongoDBでは`ObjectId`と呼ばれる１２バイトの一意な`_id`という名前の列に自動的に設定されます。
