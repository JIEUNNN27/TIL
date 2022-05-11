# 카드2
N = int(input())
card = []
for i in range(1, N+1):
    card.append(i)

# 시간초과
while len(card) != 1:
    card = card[1:]
    card.append(card[0])
    card = card[1:]
print(card[0])
