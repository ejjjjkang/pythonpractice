
#open('파일이름', '모드 / 'w : 쓰기 , R: 읽기, a: 추가/append')
f = open ('test.txt','a')

f.write('안녕하세요')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)

f.close()



