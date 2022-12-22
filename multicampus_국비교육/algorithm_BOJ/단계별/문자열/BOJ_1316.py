#그룹 단어 체커
#코드가 잘 이해가 안된다...
#https://velog.io/@cco2416/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC1316%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4
n = int(input())
count = n
for _ in range(n):
    s_list = list(input())
    s_set = set(s_list)
    for i in range(len(s_list)):
        if i > 0 and s_list[i] != s_list[i-1]:
            s_set.remove(s_list[i-1])
        if s_list[i] in s_set:
            continue
        else:
            count-=1
            break
print(count)

  