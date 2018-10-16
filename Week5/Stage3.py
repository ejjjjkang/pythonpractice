
import requests
from bs4 import BeautifulSoup
import openpyxl

req = requests.get('http://tv.naver.com/r')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')
chn_infos = {}

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '4~100 클립정보'
sheet.append(['클립 제목', '채널명', '조회수', '좋아요 수'])
sort_by_hit = wb.create_sheet('조회수별 정렬')
sort_by_hit.append(['채널명', '총 조회수', '총 좋아요 수'])


for info in infos:
    title = info.select_one('tooltip').text
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',',''))
    like = int(info.select_one('span.like').text[5:].replace(',',''))
    sheet.append([title, chn, hit, like])


    if chn in chn_infos.keys():
        chn_infos[chn]['hit'] += hit
        chn_infos[chn]['like'] += like
    else:
        chn_infos[chn] = {'hit': hit , 'like': like}


print(chn_infos)
print(chn_infos.items())

def sortByLike(item):
    return item[1]['like']

sorted_chn_infos = sorted(chn_infos.items(), key= sortByLike, reverse=True)

for i in sorted_chn_infos:
    print(i)
    sort_by_hit.append([i[0],i[1]['hit'],i[1]['like']])


wb.save('naver_tv_top100.xlsx')