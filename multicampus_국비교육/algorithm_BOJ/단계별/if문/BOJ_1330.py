#두 수 비교하기
#input int로 바꾸기 조심
a, b = map(int,input().split())

if a>b:
    print('>')
if a<b:
    print('<')
if a==b:
    print('==')