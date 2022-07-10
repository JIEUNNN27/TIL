def solution(d, budget):
    answer = 0
    d.sort()
    s=0
    for i in d:
        s += i
        answer += 1
        if s > budget:
            s = s-i
            answer = answer-1

    return answer