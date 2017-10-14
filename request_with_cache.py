import requests
from cachecontrol import CacheControl


session = requests.session()
cached_session = CacheControl(session)

# 1回目はキャッシュが無いので、サーバーから取得しキャッシュする。
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache)

# 2回目以降は、ETagとLast-Modifiedの値を使って更新されているかを確認する。
# 更新されていない場合のコンテンツはキャッシュから取得するので高速に処理できる。
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache)
