def solution(sizes):
    w = []
    h = []
    for x, y in sizes:
        w.append(max(x, y))
        h.append(min(x, y))

    return max(w) * max(h)
