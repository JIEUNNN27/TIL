# 이항 계수 1

n, k = map(int, input().split())

if k<0:
    print(0)
if k>n:
    print(0)
else:
    bunja = 1
    bunmo1 = 1
    bunmo2 = 1
    for i in range(1, n+1):
        bunja *= i
    for j in range(1, k+1):
        bunmo1 *= j
    for k in range(1, n-k+1):
        bunmo2 *= k
    print(int(bunja/(bunmo1*bunmo2)))
