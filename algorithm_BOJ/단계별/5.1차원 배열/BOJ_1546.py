#평균.
n = int(input())

guamok = list(map(int, input().split()))

guamok_max = max(guamok)
new_all_score = 0

for i in guamok:
        i = i/guamok_max*100
        new_all_score += i

print(new_all_score/n)