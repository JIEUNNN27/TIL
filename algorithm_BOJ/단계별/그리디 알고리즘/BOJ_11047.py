#BOJ 11047
#동전 0

n, k = map(int,input().split())

#동전 입력 받기
don = []
for i in range(n):
    a = int(input())
    don.append(a)

#내림차순 정렬
don_d = sorted(don, reverse = True)

y=0
x=0
for i in don_d:
    if k == 0:
        break
    elif k>=i:
        x = k//i
        y += x
        k = k - x*i
print(y)



