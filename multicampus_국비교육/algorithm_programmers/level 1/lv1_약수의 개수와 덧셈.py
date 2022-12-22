def solution(left, right):
    s = 0
    for i in range(left, right+1):
        temp = []
        for j in range(1, i+1):
            if i%j == 0:
                temp.append(j)
        if len(temp)%2 == 0:
            s += i
        else:
            s -= i

    return s