#한수
#모르겠다,,,,이해 안됨...ㅏㅏㅏㅏㅏㅏ
#----------------------------
#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
#https://blog.naver.com/pomoc153/222677139845

def hansu(num):
    num_list = list(map(int,str(num)))
    if num<100:
        return True
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        return True
    else:
        return False
    
N=int(input())
cnt=0
for i in range(1,N+1):
    if hansu(i):
        cnt+=1

print(cnt)