#OX퀴즈
#어렵다...질문검색에서 힌트
#https://www.acmicpc.net/board/view/83055

n = int(input())

ox_list = []

for i in range(n):
    ox_list.append(input())
#print(ox_list)
    sum_score = 0
    plus = 1
    for j in ox_list[i]:
        if j == 'O':
            sum_score += plus
            plus += 1
        else:
            plus = 1

    print(sum_score)