T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(a + b)


#i를 안쓰면 _표시 해도 됨
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b)
