#그룹 단어 체커
N = int(input())
cnt = 0
for _ in range(N):
    w = input()
    lst_origin = []
    lst_check = []
    for _ in w:
        lst_origin.append(_)
    for i in range(len(w)):
        if w[i] in lst_check:
            if w[i] == lst_origin[i-1]:
                lst_check.append(w[i])
        else:
            lst_check.append(w[i])
    #print(lst_check)
    #print(lst_origin)
    if lst_check == lst_origin:
        cnt +=1

print(cnt)
