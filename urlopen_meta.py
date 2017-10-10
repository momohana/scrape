import re
import sys
from urllib.request import urlopen
import requests

f = requests.get('https://gihyo.jp/dp')
bytes_content = f.text=

scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

# デコードした文字列から正規表現でcharsetの値を抜き出す。
match = re.search('charset=["\']?([\w-]+)',scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'

print('encoding:', encoding, file=sys.stderr)

text = bytes_content.decode(encoding)
print(text)
