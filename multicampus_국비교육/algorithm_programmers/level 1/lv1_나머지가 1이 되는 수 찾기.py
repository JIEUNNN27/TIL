def solution(n):
    ans_list = []
    #answer = 0
    for i in range(1, n):
        if n%i == 1:
            ans_list.append(i)
    answer = min(ans_list)        
    
    return answer