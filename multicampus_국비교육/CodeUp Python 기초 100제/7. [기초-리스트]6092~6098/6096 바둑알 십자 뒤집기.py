#검색해서...

# 바둑판 입력받아 2차원 리스트로 만들기
baduk = []
for _ in range(19):
    baduk_now = list(map(int, input().split()))
    baduk.append(baduk_now)

#십자 뒤집기 횟수
n = int(input())

#십자 뒤집기 좌표
for _ in range(n):
    x, y = map(lambda num : int(num)-1, input().split())    #인덱스가 (0, 0)으로 시작하기 때문에 -1을 한다

#십자뒤집기
#[true_value] if [condition] else [false_value]
    for i in range(19):
        baduk[i][y] = 1 if baduk[i][y] == 0 else 0
        baduk[x][i] = 1 if baduk[x][i] == 0 else 0

#출력하기        
for b in baduk:
    print(*b)

