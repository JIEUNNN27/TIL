# 나머지
num_list = [int(input()) for _ in range(10)]

namuge_list = []

for i in num_list:
    namuge = i%42
    namuge_list.append(namuge)

namuge_set = set(namuge_list)

print(len(namuge_set))