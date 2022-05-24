def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a > b:
        answer = 0
        for i in range(a-b):
            answer += b+i
        answer = answer + a
    elif b > a:
        answer = 0
        for i in range(b-a):
            answer += a+i
        answer = answer + b
    return answer