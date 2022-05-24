def solution(s):
    if s.count("p")+s.count("P") == s.count("y")+s.count("Y"):
        answer = True
    else:
        answer = False
    return answer