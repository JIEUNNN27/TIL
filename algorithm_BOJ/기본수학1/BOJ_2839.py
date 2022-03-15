#설탕 배달
#https://blog.naver.com/sag120/222569112296

N = int(input())

a = 0
while True:
    if N%5 == 0:
        N = N-5
        a += 1
    elif N%3 == 0:
        N = N-3
        a += 1
    else:
        N = N-3
        a += 1
    
    if N == 0:
        break
    if N < 0:
        a = -1
        break
print(a)