#다이얼
#들여쓰기 조심하자...
word = input()
wl = []
for i in word:
    wl.append(ord(i))

t=0
for i in wl:

    for j in range(5):
        if i == 65+(3*j) or i == 66+(3*j) or i == 67+(3*j):
            t = t + 3+j
        
    if i == 80 or i == 81 or i == 82 or i == 83:
        t = t + 8

    if i == 84 or i == 85 or i == 86:
        t = t + 9

    if i == 87 or i == 88 or i == 89 or i == 90:
        t = t + 10

print(t)

