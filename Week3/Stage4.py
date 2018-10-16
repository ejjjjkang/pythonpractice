import requests
from bs4 import BeautifulSoup

dictionary = {}


for i in range(1, 4):
    res = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=2018+여의도+불꽃축제&start=' + str(i * 10 + 1), headers={'User-Agent': 'Mozilla/5.0'})
    raw = res.text
    html = BeautifulSoup(raw, 'html.parser')

    articles = html.select('ul.type01 > li')

    for article in articles:
        title = article.select_one('a._sp_each_title').text
        journal = article.select_one('span._sp_each_source').text
        print(title, '/', journal)

    print('---------', i, '페이지 수집중', '----------')