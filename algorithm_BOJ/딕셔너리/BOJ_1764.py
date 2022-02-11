#듣보잡
n, m = map(int,input().split())
diname = {}
kk =[]

#듣x(d)
for i in range(n):
    name = input()
    diname[name] = 'd'

#보x(b)
#만약 듣x에 이름이 있으면 듣보(db)로 수정
for i in range(m):
    name=input()
    if name in diname:
        diname[name] = 'db'
    else:
        diname[name] = 'b'

#듣보만 따로 모으기
for key, val in diname.items():
    if val == 'db':
        kk.append(key)

#출력
print(len(kk))
print(*sorted(kk), sep ='\n')
