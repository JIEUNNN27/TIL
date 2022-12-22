a, m, d, n = map(int, input().split())
x=a
for i in range(1, n):
    x = x*m+d
print(x)