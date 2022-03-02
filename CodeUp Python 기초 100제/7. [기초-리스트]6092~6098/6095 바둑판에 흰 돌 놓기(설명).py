#구글링해서......
d = [[0 for i in range(19)] for i in range(19)]

#흰 돌의 갯수
n = int(input())

#흰 돌을 놓을 좌표, 흰돌 = 1으로 설정
for _ in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1

#바둑판 출력
for i in range(19):
    for j in range(19):
        print(d[i][j], end = " ")
    print()
