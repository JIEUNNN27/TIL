def solution(n):

    if int(n**(1/2))**2 == n:
        answer = (int(n**(1/2))+1)**2
    else:
        answer = -1

    return answer


####이거 안됨#######
# def solution(n):
#     po = -1
#     for i in range(1,n):
#         if n/i == i:
#             po = (i+1)**2

#     return po
