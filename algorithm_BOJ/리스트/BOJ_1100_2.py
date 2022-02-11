#하얀칸
#주석 없는 버전
pan = [list(input()) for _ in range(8)]
mal_all = 0

for k in range(8):
    for s in range(8):
        if k%2 == s%2 and pan[k][s] == 'F':
            mal_all += 1

print(mal_all)