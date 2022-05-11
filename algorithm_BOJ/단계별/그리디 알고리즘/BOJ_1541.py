# 잃어버린 괄호
# -단위로 묶어서 쪼개기
sik = input().split('-')
# print(sik)

su_sum = 0

# 맨 앞에는 더한다(맨앞은 +만 있으니까...)
for i in sik[0].split('+'):
    su_sum += int(i)

# +로 나눠서 각각 빼주기
for j in sik[1:]:
    for k in j.split('+'):
        su_sum -= int(k)

print(su_sum)

# 이거 안됨
# plus = []
# for i in sik:
#     #pl = i.split('+')
#     pl_sum = 0
#     for j in i.split('+'):
#         j = int(j)
#         pl_sum += j
#     plus.append(pl_sum)

# # print(plus)
