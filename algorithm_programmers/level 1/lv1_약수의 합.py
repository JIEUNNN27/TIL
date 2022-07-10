def solution(n):
    yak = []
    for i in range(1,n+1):
        if n%i == 0:
            yak.append(i)
            
    answer = sum(yak)
    return answer