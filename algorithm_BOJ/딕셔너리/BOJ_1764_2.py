#듣보잡
n, m = map(int,input().split())
diname = {}
kk =[]

#듣x(d)
for i in range(n+m):
    name = input()
    if name in diname:
        diname[name] =+ 1
    else:
        diname[name] = 0
#print(diname)

for key, val in diname.items():
    if val == 1:
        kk.append(key)

print(len(kk))
print(*sorted(kk), sep = '\n')


