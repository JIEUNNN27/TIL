def solution(n, arr1, arr2):
    answer = ['' for i in range(n)]
    for j in range(n):
        a = arr1[j]
        b = arr2[j]
        for k in range(n):
            if a%2 + b%2 > 0:
                answer[j] = '#' + answer[j]
            else:
                answer[j] = ' ' + answer[j]
            a = a//2
            b = b//2
    
    return answer