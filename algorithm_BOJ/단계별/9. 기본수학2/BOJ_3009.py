#네 번째 점
#https://blog.naver.com/sua0211/222663579163


#숫자 받아서 리스트 만들기
xl = []
yl = []

for _ in range(3):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)

#1개인 좌표 찾기
for i in range(3):
    if xl.count(xl[i]) == 1:
        a = xl[i]
    if yl.count(yl[i]) == 1:
        b = yl[i]

print(a, b)

