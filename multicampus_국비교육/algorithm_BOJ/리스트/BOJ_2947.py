#나무조각
namu = [int(i) for i in input().split()]

while namu != [1, 2, 3, 4, 5]:
    for i in range(4):
        if namu[i] > namu[i+1]:
            a = namu[i]
            b = namu[i+1]
            namu[i] = b
            namu[i+1] = a
            
            print(*namu)
    

