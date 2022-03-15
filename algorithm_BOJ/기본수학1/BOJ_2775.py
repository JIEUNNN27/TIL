#부녀회장이 될테야
#https://blog.naver.com/mkdusgml/222249652446 참고...


T = int(input())
for _ in range(T):
    fl = int(input())
    ho = int(input())
    pp = [_ for _ in range(1, ho+1)]
    for i in range(fl):
        for j in range(ho-1):
            pp[j+1] += pp[j]        #이부분이 이해가 잘 안된다...
    print(pp[-1])
    #print(pp)

