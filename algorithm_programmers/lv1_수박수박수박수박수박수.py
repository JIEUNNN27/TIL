def solution(n):
    answer = ''
    #홀수
    if n%2 == 1:
        answer = "수박"*(n//2) + "수"
    #짝수
    else:
        answer = "수박"*(n//2)
    return answer