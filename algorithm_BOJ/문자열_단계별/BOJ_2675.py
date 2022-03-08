T = int(input())

for i in range(T):
    r, s = input().split()
    for ss in s:
        print(ss*int(r),end='')
    print("")