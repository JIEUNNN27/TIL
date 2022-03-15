#직각삼각형
a = 1
while a != 0:
    numl = list(map(int, input().split()))
    numl.sort()
    
    a = numl[0]*numl[0]
    b = numl[1]*numl[1]
    c = numl[2]*numl[2]

    if a == 0:
        break

    if a + b == c:
        print('right')
    else:
        print('wrong')
