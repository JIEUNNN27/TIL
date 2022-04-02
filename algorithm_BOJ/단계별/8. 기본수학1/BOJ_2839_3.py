n=int(input())
x=0

if n%5==0:
    print(n//5)
else:
    while n>=0:
        x+=1
        n-=3
        if n%5==0:
            print(n//5+x)
            break
    if n%5==0:
        print()
    elif n%3==0:
        print(n//5+(n//3))
    else:
        print(-1)
