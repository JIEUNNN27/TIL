#나는 요리사다
cook = [[int(i) for i in input().split()] for _ in range(5)]

su = [sum(w) for w in cook]
print(su.index(max(su))+1, max(su))