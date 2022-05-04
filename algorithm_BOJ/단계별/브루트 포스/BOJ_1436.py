# BOJ 1436
# 영화 감독 숌

n = int(input())

x = 0
y = 0

while y!=n:
    x+=1
    str_x = str(x)
    if '666' in str_x:
        y += 1

print(str_x)