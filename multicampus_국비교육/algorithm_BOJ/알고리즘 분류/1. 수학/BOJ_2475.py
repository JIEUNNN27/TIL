#검증수

num_lst = map(int, input().split())

sum = 0

for i in num_lst:
    sum += i*i

print(sum%10)