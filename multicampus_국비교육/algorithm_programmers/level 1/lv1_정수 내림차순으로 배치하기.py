def solution(n):
    num_list = []
    for i in str(n):
        num_list.append(i)
    s_num_list = sorted(num_list, reverse=True)

    #answer = ''.join(s_num_list)
    answer = int(''.join(s_num_list))

    return answer
