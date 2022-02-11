#별찍기 - 20
N = int(input())

for i in range(1,N+1):
    if i%2 == 1:
        print('* '*N)
    else:
        print(' '+'* '*N)



# n = int(input())

# for i in range(n):
#     if i % 2 == 0:
#         print('* '* n)
#     else:
#         print(' *'* n)
    
#     #한줄로 쓰기
#     print("* "*n if i %2 == 0 else ' *'*n)