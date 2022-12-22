#https://blog.naver.com/idmanddang/222710987814
#지이이이인짜 모르겠어서 이거 참고하고 했어요...
#n%i=0 안됨....

def solution(n):
    answer = set(range(2, n+1))
    for i in range(2, n//2 + 2):
        answer -= set(range(2*i, n+1, i))

    return len(answer)