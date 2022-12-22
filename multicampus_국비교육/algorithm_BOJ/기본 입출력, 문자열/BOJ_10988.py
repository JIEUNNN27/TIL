#팰린드롬인지 확인하기
#팰린드롬 : 앞으로 읽을 때와 거꾸로 읽을 때가 똑같은 단어
p = str(input())
if p == p[::-1]:
    print(1)

else:
    print(0)

#word = intput()
#print(int(word == word[::-1]))