#A+B-4
#try, except 적극 활용하기!!
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break