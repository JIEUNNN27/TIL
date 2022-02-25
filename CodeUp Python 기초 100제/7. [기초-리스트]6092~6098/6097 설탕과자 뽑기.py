#이것도 검색해서...
# 가로 세로 입력
h,w= map(int,input().split())

# 격자판 생성
m = []
for i in range(h+1):#가로 '길이'
  m.append([])
  for j in range(w+1):
    m[i].append(0)

# 길이,가로세로여부,좌표 받아서 올려놓기
n = int(input())
for i in range(n):
  l,d,x,y=map(int,input().split())
  for j in range(l):
     if d == 0:
         m[x-1][y-1+j] = 1 # 격자판의 좌표의 원점이 1,1임을 유의하기. 그러나 리스트의 원점칸은 0,0 따라서 -1해줌
     else:
         m[x-1+j][y-1] = 1

#격자판 출력
for i in range(h):
  for j in range(w):
    print(m[i][j],end = ' ')
  print()