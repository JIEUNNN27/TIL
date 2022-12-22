namu = [int(i) for i in input().split()]

while namu != [1, 2, 3, 4, 5]:
    for i in range(4):
        if namu[i] > namu[i+1]:
            namu[i], namu[i+1] = namu[i+1],namu[i] 
            
            print(*namu)