def solution(x):
    y = str(x)
    y_sum = 0

    for i in range(len(y)):
        int_i = int(y[i])
        y_sum += int_i
    if x % y_sum == 0:
        answer = True
    else:
        answer = False
    return answer
