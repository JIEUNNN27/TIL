def solution(s):
    x = len(s)
    if x%2 == 1:
        answer = s[x//2]
    elif x%2 == 0:
        answer = s[int(x//2)-1]+s[int(x//2)]
    return answer