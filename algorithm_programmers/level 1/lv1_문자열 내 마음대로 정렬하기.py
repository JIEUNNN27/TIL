def solution(strings, n):
    strings.sort(key = lambda i: (i[n],i))
    return strings
