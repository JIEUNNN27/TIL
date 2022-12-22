#220707(목)
N = int(input())
info = []

for i in range(N):
    w, h = list(map(int, input().split(' ')))
    info.append([w,h])

for j in info:
    rank = 1
    for k in info:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
        else:
            pass
    print(rank, end = ' ')
