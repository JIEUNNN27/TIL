# 샹수
a, b = input().split()

ra = a[2]+a[1]+a[0]
rb = b[2]+b[1]+b[0]

lst = []
lst.append(int(ra))
lst.append(int(rb))

print(max(lst))