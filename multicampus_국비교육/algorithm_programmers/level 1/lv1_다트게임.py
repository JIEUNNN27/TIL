def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'x')
    dart = list(dartResult)
    for i in range(len(dart)):
        if dart[i] == 'x':
            dart[i] = 10
            
    for i in range(1, len(dart)):
        if dart[i] == 'S':
            answer.append(int(dart[i-1]))
        elif dart[i] == 'D':
            answer.append(int(dart[i-1])**2)
        elif dart[i] == 'T':
            answer.append(int(dart[i-1])**3)
            
    for i in range(2, len(dart)):
        if dart[i] == '*':
            if i == 2:
                answer[0] *= 2
            elif 3 < i < 6:
                answer[0] *= 2
                answer[1] *= 2
            else:
                answer[1] *= 2
                answer[2] *= 2
        elif dart[i] == '#':
            if i == 2:
                answer[0] *= -1
            elif 3 < i < 6:
                answer[1] *= -1
            else:
                answer[2] *= -1
    
    return sum(answer)



# 이거 안됨
# def solution(dartResult):
#     answer = []
#     score_list = []
#     dartResult = dartResult.replace('10', 'x')
#     for i in dartResult:
#         score_list.append(str(i))
 
#     for i in range(len(score_list)):
#         if score_list[i] == 'x':
#             score_list[i] = 10
            
#     for i in range(1, len(score_list)):
#         if score_list[i] == 'S':
#             answer.append(int(score_list[i-1]))
#         elif score_list[i] == 'D':
#             answer.append(int(score_list[i-1]**2))
#         elif score_list[i] == 'T':
#             answer.append(int(score_list[i-1]**3))
    
#     for i in range(2, len(score_list)):
#         if score_list[i] == '*':
#             if i == 2:
#                 answer[0] *= 2
#             elif 3 < i < 6:
#                 answer[0] *= 2
#                 answer[1] *= 2
#             else:
#                 answer[1] *= 2
#                 answer[2] *= 2
#         elif score_list[i] == '#':
#             if i == 2:
#                 answer[0] *= -1
#             elif 3 < i < 6:
#                 answer[1] *= -1
#             else:
#                 answer[2] *= -1
                    
#     return sum(answer)