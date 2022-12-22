#팩토리얼
from re import I


N = int(input())

n = 1
for i in range(1, N+1):
    n *=i

print(n)