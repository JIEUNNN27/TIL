a, b = map(int,input().split())
c=int(input())

t=a*60+b+c

x = t//60
y = t%60

if x>=24:
    print(t//60-24, t%60)
else:
    print(t//60, t%60)