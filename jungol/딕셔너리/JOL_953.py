#기타 자료형 - 형성평가6
baseball = input().split() #초기화


#딕셔너리 만들기
dbaseball = {} #초기화

for i in baseball:
    dbaseball[i] = baseball.count(i)


#파울 적게 한 선수 골라서 프린트 하기
#.items() 활용
minf =min(dbaseball.values())
for key, val in dbaseball.items():
    if val == minf:
        print(key)

print(minf)