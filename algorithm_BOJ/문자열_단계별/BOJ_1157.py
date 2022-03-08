#단어 공부
word = input()

UW = word.upper()

Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

al_num = [0]*26


for i in range(len(Alpha)):
    c = 0
    al_num[i] = UW.count(Alpha[i])
    
#print(al_num)
#print(max(al_num))
m = max(al_num)
index_m = al_num.index(m)


if al_num.count(m) >= 2:
    print('?')
else:
    print(Alpha[index_m])