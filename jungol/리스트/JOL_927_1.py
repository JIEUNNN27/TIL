#리스트3 - 자가진단7
score = [list(map(int,input().split())) for i in range(5)]
p = 0

for s in score:
    m = sum(s)/4
    if m >=80:
        p += 1
        print('pass')
    else:
        print('fail')
print(f'Successful : {p}')
