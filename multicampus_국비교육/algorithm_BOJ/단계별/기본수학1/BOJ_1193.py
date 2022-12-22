#분수찾기
#https://blog.naver.com/jhe226/222451280818 참고
X = int(input())

cnt = 0
up = 0
end = 0
while X > end:
    up += 1
    cnt += 1
    end += up

#홀수줄
if cnt%2 == 1:
    print(f'{end-X+1}/{cnt-end+X}')
#짝수줄
else:
    print(f'{cnt-end+X}/{end-X+1}')
