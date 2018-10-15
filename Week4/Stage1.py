
# ---- dictionary 기본 구성 & 조회 ---

people = {'korean': 380, 'american': 42, 'japanese': 15}


print(people)
print(people['korean'])


# ---- 중첩 dictionary 구조 ----

chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 3500},
            '쇼미더머니7': {'hit': 25000, 'like': 2200}}

print(chnInfos['미스터션샤인']['hit'])

#새로운 데이터 추가

chnInfos['아빠어디가'] = {'hit':3000}

#dic 데이터를 리스트로 만들어주는 것
print(chnInfos.keys())
print(chnInfos.values())
chnitems = chnInfos.items()

for item in chnitems:
    print(item)