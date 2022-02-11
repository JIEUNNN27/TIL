#색종이

#도화지를 만든다.(0으로)
paper = [[0]*100 for _ in range(100)]

#색종이 칠하기
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1     #색칠

#영역의 넓이 출력(도화지에서 1인 부분을 그냥 다 더한다)

s = 0
for i in range(100):
    for j in range(100):
        s += paper[i][j]

#total = sum(sum(line) for line in paper)

print(s)