def solution(board, moves):
    baguni = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                baguni.append(board[j][i-1])
                board[j][i-1] = 0

                if len(baguni) > 1:
                    if baguni[-1] == baguni[-2]:
                        baguni.pop(-1)
                        baguni.pop(-1)
                        answer += 2     
                break

    return answer