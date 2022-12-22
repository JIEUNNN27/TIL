#220706 수요일
#-------시간초과--------
N = int(input())
num_lst = []

#입력받기
for i in range(N):
    num_lst.append(input())

#오름차순 정렬
num_lst.sort()

#unpacking 활용하여 출력하기
print(*num_lst, sep='\n')

#-----------입력을 sys로 바꿔주기----------------   
import sys

N =  int(sys.stdin.readline())
nums = []

#입력
for i in range(N):
    nums.append(int(sys.stdin.readline()))

#오름차순 정렬
nums.sort()

#출력
print(*nums, sep='\n')