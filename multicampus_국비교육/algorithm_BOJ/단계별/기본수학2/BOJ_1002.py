# 터렛
import math
n = int(input())

d = 0
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    #완벽히 똑같은 원
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    #포함관계
    elif d+r2 < r1 or d+r1 < r2:
        print(0)
    #서로 멀리 떨어져 있는 관계
    elif d > r1+r2:
        print(0)
    #접할 때
    elif d == r1+r2 or r2+d == r1 or r1+d == r2:
        print(1)
    #두점에서 만날 때
    elif d < r1+r2:
        print(2)
    
    
    

            


