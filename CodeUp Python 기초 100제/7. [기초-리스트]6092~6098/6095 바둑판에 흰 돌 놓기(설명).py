#구글링해서......
d = [[0 for i in range(19)] for i in range(19)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1


for i in range(19):
    for j in range(19):
        print(d[i][j], end = " ")
    print()
