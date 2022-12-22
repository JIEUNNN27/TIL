#주사위 세개
a, b, c = map(int, input().split())

#1등
if a == b == c:
    print(10000+a*1000)

#2등
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)

#3등
else:
    x = max(a, b, c)
    print(x*100)