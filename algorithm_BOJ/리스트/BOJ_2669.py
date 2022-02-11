#직사각형 네개의 합집합의 면적 구하기
paper = [[0]*100 for _ in range(100)]

for i in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            paper[i][j] = 1

s = 0
for i in range(100):
    for j in range(100):
        s += paper[i][j]
print(s)

        
