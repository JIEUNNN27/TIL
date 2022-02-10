# 하얀 칸(2차원 리스트 연습 문제)
pan = [list(input()) for _ in range(8)]
#print(pan)
mal_all = 0

#체스판을 모두 돌아다니면서 조건 확인

#조건 => 짝수 줄의 짝수 칸 or 홀수 줄의 홀수 칸
# i : 가로, j: 세로
for i in range(8):
    for j in range(8):
        #가로로 탐색하기
        if i %2 == j % 2 and pan[i][j] == 'F':
            mal_all += 1
        #세로로 탐색하기 ([j][i]로 인덱스 바꾸기)
        #if i %2 == j % 2 and pan[j][i] == 'F':

print(mal_all)





    
    
    
    


