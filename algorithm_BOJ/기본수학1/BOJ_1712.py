#손익분기점
a, b, c = map(int,input().split())

#x = 판매량

if c != b:
    x = a/(c-b)
    
    if x>0:
        print(int(x+1))
    else:
        print(-1)
else:
    print(-1)