#검색해서...
# 바둑판 만들기
baduk = []
for _ in range(19):
    matrix = list(map(int, input().split()))
    baduk.append(matrix)

# 십자 형태에 맞춰 뒤집기
n = int(input())
for _ in range(n):

# 바둑판의 인덱스는 (0,0)으로 시작하기 때문에 -1을 해준다.
    x, y = map(lambda num : int(num)-1, input().split())

# 삼항 연산자 : [true_value] if [condition] else [false_value]
    for i in range(19):
        baduk[i][y] = 1 if baduk[i][y] == 0 else 0
        baduk[x][i] = 1 if baduk[x][i] == 0 else 0
        
for b in baduk:
    print(*b)

