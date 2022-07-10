def solution(n):
    answer = []
    for i in range(len(str(n))-1, -1, -1):
        answer.append(int(str(n)[i]))

    # 이거해서 reverse는 안됨
    # n_list = []
    # for i in str(n):
    #     n_list.append(int(i))

    return answer
