def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].isupper():
            x = ord(s[i])+n
            if x>90 :
                answer += chr(64+x-90)
            else:
                answer += chr(x)
                
        elif s[i].islower():
            x = ord(s[i])+n
            if x>122:
                answer += chr(96+x-122)
            else:
                answer += chr(x)
        elif s[i] == ' ':
            answer += " "
        
            
    return answer