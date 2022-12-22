a, b, c, d = map(int, input().split())
print(round(a*b*c*d/8/1024/1024, 1), 'MB')