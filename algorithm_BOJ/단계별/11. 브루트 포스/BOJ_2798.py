#블랙잭
#https://blog.naver.com/1018gustj/222639440848

#for문 중첩시키기...
n, m = map(int,input().split())

card = list(map(int, input().split()))

lst = []    #합을 저장할 리스트

#카드는 3장 뽑으니까...
#M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해서 출력하기
for i in range(n-2):
    for j in range(i+1, n-1): #i보다 한칸 뒤부터
        for k in range(j+1, n): #i보다 두칸 뒤부터
            if card[i] + card[j] + card[k] > m:
                continue   #합이 M보다 크면 안됨
            else:
                lst.append(card[i] + card[j] + card[k])

#m값을 넘지 않는 수 중에서 가장 큰 값을 출력
print(max(lst))

