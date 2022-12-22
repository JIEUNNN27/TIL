#수 정렬하기(내장함수 연습 문제)
n = int(input())
nums = [int(input()) for _ in range(n)]

print(*sorted(nums), sep = '\n')

