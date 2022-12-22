#오타맨 고창영
T =int(input())
for i in range(T):
    n, s = input().split()
    print(s[:int(n)-1] + s[int(n):])

# for _ in range(int(input())):
#     index, word = input().split()
#     index = int(index)
#     print(word[:index-1] + word[index:])
