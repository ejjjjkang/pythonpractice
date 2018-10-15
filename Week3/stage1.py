import requests
from bs4 import BeautifulSoup

req = requests.get('https://tv.naver.com/r')

raw = req.text
html = BeautifulSoup(raw, 'html.parser')
cnn_infos = html.select('div.cds')

for info in cnn_infos:
    title = info.select_one('tooltip').text
    hit = info.select_one('span.hit').text
    like = info.select_one('span.like').text

    print(title,hit,like)


