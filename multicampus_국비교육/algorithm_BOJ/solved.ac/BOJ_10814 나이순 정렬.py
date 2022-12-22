#220708 금
# N = int(input())
# lst = []
# for _ in range(N):
#     age, name = input().split()
#     lst.append([int(age), name])

# lst.sort(key=lambda x: x[0])

# for info in lst:
#     print(info[0], info[1])

# 시간 단축
import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    lst.append([int(age), name])

lst.sort(key=lambda x: x[0])

for info in lst:
    print(info[0], info[1])

