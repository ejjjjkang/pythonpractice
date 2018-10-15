
import requests
from bs4 import BeautifulSoup

req = requests.get('http://tv.naver.com/r')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')
chn_infos = {}


for info in infos:
    title = info.select_one('tooltip').text
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',',''))
    like = int(info.select_one('span.like').text[5:].replace(',',''))
    score = (hit + like * 350) // 100 #//소수점없애기


    if chn in chn_infos.keys():
        chn_infos[chn]['hit'] += hit
        chn_infos[chn]['like'] += like
        chn_infos[chn]['score'] += score
    else:
        chn_infos[chn] = {'hit': hit , 'like': like, 'score': score}

def sortByScore(item):
    return item[1]['score']

sorted_chn_infos = sorted(chn_infos.items(), key=sortByScore, reverse=True)

for i in sorted_chn_infos:
    print(i)