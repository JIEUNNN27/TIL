def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        #'true', 'True' 안됨..True로 해야 됨
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
    
