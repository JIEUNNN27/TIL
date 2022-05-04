#ACM 호텔
#https://blog.naver.com/rupi766/222386476472 참고

t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())
    fl = 0
    ho = 0
    if n%h == 0:
        ho = n//h
        fl = h*100
    else:
        ho = n//h + 1
        fl = n%h * 100
    print(fl+ho)
