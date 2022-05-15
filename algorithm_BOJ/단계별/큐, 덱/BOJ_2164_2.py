# 카드2
# 덱에 대한 설명 : https://mong9data.tistory.com/50

from collections import deque
N = int(input())


d = deque()

for i in range(1, N+1):
    d.append(i)

while len(d) != 1:
    # 맨 앞의 카드 삭제
    d.popleft()
    # 두번째 카드 맨 뒤로 보내기
    x = d.popleft()
    d.append(x)

print(d[0])
