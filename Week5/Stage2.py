
import requests
from bs4 import BeautifulSoup
import datetime

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

    if chn in chn_infos.keys():
        chn_infos[chn]['hit'] += hit
        chn_infos[chn]['like'] += like
    else:
        chn_infos[chn] = {'hit': hit , 'like': like}


print(chn_infos)
print(chn_infos.items())

def sortByLike(item):
    return item[1]['like']

sorted_chn_infos = sorted(chn_infos.items(), key=sortByLike)

dt = datetime.datetime.now()
filename = dt.strftime('%Y_%m_%d')

#CSV는 쉼표밖에 구분을 못한다
f = open(filename + '.csv', 'w')

for i in sorted_chn_infos:
    print(i)
    f.write(i[0] + ',' + str(i[1]['hit']) + '\n')

f.close()