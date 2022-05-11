def solution(num):
    c = 0
    while num != 1:
        if num % 2 == 0:
            num = num/2
            c += 1
        else:
            num = num*3 + 1
            c += 1

    if c < 500:
        return c
    else:
        return -1
