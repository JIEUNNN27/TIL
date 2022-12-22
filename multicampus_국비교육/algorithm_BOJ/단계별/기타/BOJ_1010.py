#다리놓기
# mCn (조합) 공식 구현하기

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    elif N == 1:
        print(M)
    else:
        bunza = 1
        bunmo1 = 1
        bunmo2 = 1
        for i in range(1, M+1):
            bunza *= i
        for j in range(1, N+1):
            bunmo1 *= j
        for k in range(1, M-N+1):  #아..이거..+1....
            bunmo2 *= k
        print(int(bunza/(bunmo1*bunmo2)))
        