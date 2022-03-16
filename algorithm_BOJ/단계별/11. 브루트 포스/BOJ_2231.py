#분배합
#https://blog.naver.com/mkdusgml/222408005569

result = 0
answer = []

n = int(input())

for i in range(n):
    digits = list(str(i))
    result = i

    for j in digits:
        result += int(j)
    
    if result == n:
        answer.append(i)

if len(answer):
    print(min(answer))
else:
    print(0)