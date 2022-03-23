#소수 찾기

#입력받을 숫자의 개수
N = int(input())
nums = list(map(int, input().split(' ')))

#소수의 갯수
sosu = 0


for i in nums:
    cnt = 0
    if i == 1:
        continue

    #소수 찾기
    for j in range(2, i+1):
        if i % j == 0:
            cnt +=1
    if cnt == 1:
        sosu += 1

print(sosu)
