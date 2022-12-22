# 터렛
import math
n = int(input())

s = 0
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    s = math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    #완벽히 똑같은 원
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    #포함관계
    elif s+r2 < r1 or s+r1 < r2:
        print(0)
    #서로 멀리 떨어져 있는 관계
    elif s > r1+r2:
        print(0)
    #접할 때
    elif s == r1+r2 or r2+s == r1 or r1+s == r2:
        print(1)
    #두점에서 만날 때
    elif s < r1+r2:
        print(2)
    
    
    

            


