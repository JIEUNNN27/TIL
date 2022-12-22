def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
#이거 안됨
#     temp = []
#     for i in phone_number:
#         temp.append(i)
    
#     temp[:-4] = '****'
    

#     for i in temp:
#         answer = print(i,sep='',end='')
        
    return answer