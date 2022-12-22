def solution(numbers):
    plus_list = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                pass
            else:
                plus_list.append(numbers[i]+numbers[j])
    plus_set = set(plus_list)

    answer = list(plus_set)
    answer = sorted(answer)
    return answer
