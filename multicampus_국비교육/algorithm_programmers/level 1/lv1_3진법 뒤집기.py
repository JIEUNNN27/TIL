def solution(n):
    x = ''
    while n:
        n, b = divmod(n,3)
        x += str(b)
    answer = int(x, 3)
    return answer