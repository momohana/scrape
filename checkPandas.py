import pandas as pd

pd.read_csv('data/exchange.csv')
# 問題発生。対応のためのコードは以下のとおり。
df_exchange = pd.read_csv('data/exchange.csv', header=1, names=['date', 'USD', 'rate'], skipinitialspace=True, index_col=0, parse_dates=True)
print(df_exchange)

from datetime import datetime

def parse_japanese_date(s):
    # 昭和、平成の０年に相当する年を定義しておく。
    base_years = {'S':1925, 'H':1988}
    # 元号を表すアルファベット１文字を取得。
    era = s[0]
    # 2文字目以降を.で分割して年月日に分ける。
    year,month,day = s[1:].split('.')
    # 元号の０年に相当する年と数値に変換した年を足して西暦の年を得る。
    year = base_years[era] + int(year)
    return datetime(year, int(month), int(day))

parse_japanese_date('S49.9.24')
 parse_japanese_date('H27.5.5')

df_jgbcm = pd.read_csv('data/jgbcm_all.csv', index_col=0, parse_dates=True,date_parser=parse_japanese_date, na_values=['-'])

df_jobs = pd.read_excel('data/第3表.xls', skiprows=3, skip_footer=2, parse_cols='W,Y:AJ', index_col=0)

df_jobs

s_jobs = df_jobs.stack()
s_jobs
list(s_jobs.index)
def parse_year_and_month(year,month):
    year = int(year[:-1])
    month = int(month[:-1])
    year += (1900 if year >= 63 else 2000)
    return datetime(year, month, 1)

parse_year_and_month('63年', '１月')
parse_year_and_month('16年', '3月')

s_jobs.index = [parse_year_and_month(y, m) for y, m in s_jobs.index]
s_jobs
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,4,9,16,25])
plt.show()
