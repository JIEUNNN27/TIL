def solution(s):
    s_list = s.split(' ')
    #a_list = [] 리스트로 하니까 곤란해짐-> 문자열로!
    a = ''
    for i in s_list:
        for j in range(len(i)):
            if j%2 == 0:
                a += i[j].upper()
            else:
                a += i[j].lower()
        a += ' '
   
    return a[:-1]