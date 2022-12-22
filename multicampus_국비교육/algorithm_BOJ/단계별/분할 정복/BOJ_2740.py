# 행렬 곱셈

# 인풋 받기
# 행렬 A
N, M = map(int, input().split())
array1 = [list(map(int, input().split())) for _ in range(N)]
# 행렬 B
M, K = map(int, input().split())
array2 = [list(map(int, input().split())) for _ in range(M)]

# print(array2)

# 결과 리스트 만들기(빈 리스트)
result = [[0]*K for _ in range(N)]

# 행렬 곱..
# 손으로 계산할때 그 행렬곱 공식 이용함...
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += array1[i][k] * array2[k][j]

# print(result)
for i in result:
    print(*i)
