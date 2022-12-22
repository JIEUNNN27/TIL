#벌집
N = int(input())
nums = N-1


if nums == 0:
    print(1)
else:
    i = 1
    n = 0
    while nums >= i:
        n += 1
        i += 6 * n
    print(n + 1)
        