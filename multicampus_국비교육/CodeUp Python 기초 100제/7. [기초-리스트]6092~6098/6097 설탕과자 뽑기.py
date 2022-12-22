#이것도 검색해서...
#격자판의 가로, 세로 받기
h,w= map(int,input().split())

# 격자판 만들기
m = []
for i in range(h+1): #가로 '길이'니까 +1
  m.append([])
  for j in range(w+1): #세로 '길이'니까 +1
    m[i].append(0)


#놓을 수 있는 막대 개수
n = int(input())

for i in range(n):
  l,d,x,y=map(int,input().split())    #막대의 길이, 방향, 좌표
  for j in range(l):
     if d == 0:  #가로
         m[x-1][y-1+j] = 1 #리스트의 원점칸은 0,0 따라서 -1해줌
     else:  #세로
         m[x-1+j][y-1] = 1

#격자판 출력
for i in range(h):
  for j in range(w):
    print(m[i][j],end = ' ')
  print()