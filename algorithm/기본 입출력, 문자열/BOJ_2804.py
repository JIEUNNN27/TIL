#크로스워드 만들기
A,B = input().split()
#A와 B의 문자 길이
N = len(A)
M = len(B)

for i in range(N):
    if A[i] in B:
        aa = i
        bb = B.index(A[i])
        break

for i in range(M):
    if i == bb:
        print(A)
    else:
         print('.'*aa+B[i]+'.'*(N-aa-1))