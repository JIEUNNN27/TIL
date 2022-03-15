#달팽이는 올라가고 싶다
#https://blog.naver.com/findwuw/222518602069 참고
u, dwn, namu = map(int,input().split())

# day = 0
# l = 0
# while l < namu:
#     day +=1
#     l = (u-dwn)*day
#     if l>=namu:
#         break

# if l == namu:
#     print(day-1)
# else:
#     print(day)
from math import *
day = ceil((namu-u)/(u-dwn)+1)
print(int(day))