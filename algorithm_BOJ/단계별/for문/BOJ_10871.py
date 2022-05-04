#X보다 작은 수
a, b = map(int, input().split())
nl = list(map(int, input().split()))

for i in nl:
    if i < b:
        print(i, end=' ')