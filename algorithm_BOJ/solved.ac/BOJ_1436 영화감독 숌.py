#220704(월)
n = int(input())

x = 0
y = 0

#1부터 세면서(x) 666이 있으면 y번째 추가해주기
while y!=n:
    x+=1
    str_x = str(x)
    if '666' in str_x:
        y += 1

print(str_x)