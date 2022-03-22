#행렬 곱셈
N, M = map(int, input().split())
array1 = [list(map(int, input().split())) for _ in range(N)]


M, K = map(int, input().split())
array2 = [list(map(int, input().split())) for _ in range(M)]

#print(array2)

#결과를 지정해줄 리스트 만들기
result = [[0]*K for _ in range(N)]

#행렬 곱
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += array1[i][k] * array2[k][j]

#print(result)
for i in result:
    print(*i)