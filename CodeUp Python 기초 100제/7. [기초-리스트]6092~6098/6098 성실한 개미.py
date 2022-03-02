#검색해서..
#https://blog.naver.com/happy_faces/222339428675

d=[list(map(int,input().split())) for _ in range(10)]   #입력을 2차원 리스트로 받기
x=1
y=1

while d[x][y]!=2:   #먹이를 찾을 때 까지 반복
    while d[x][y]==0:   #0일때 계속해서 개미는 이동한다
        d[x][y]=9
        y+=1
    if d[x][y]==2:  #개미가 오른쪽으로 가다가 먹이를 찾으면 조건문의 반복을 중지하고 다음으로 넘어감
        d[x][y]=9
        break    
    x=x+1   #개미가 0이 아닐때 즉 벽을 만나거나 먹이를 만날때 아래로 진행하는 것을 의미함
    y=y-1
    if d[x][y]==2:  #개미가 아래로 내려가다가 먹이를 찾을 경우 반복을 중지하고 다음으로 넘어감
        d[x][y]=9
        break
        
    if d[x][y]==1:  #개미가 아래길도 막혀있으면 멈추는 것을 의미
        break
    
#출력
for i in range(10):
    for j in range(10):
        print(d[i][j],end=' ')
    print()
