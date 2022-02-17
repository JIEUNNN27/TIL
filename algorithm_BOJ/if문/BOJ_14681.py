#사분면 고르기
x,y = [int(input()) for _ in range(2)]

if x>0 and y>0:
    print(1)
if x<0 and y>0:
    print(2)
if x<0 and y<0:
    print(3)
if x>0 and y<0:
    print(4)