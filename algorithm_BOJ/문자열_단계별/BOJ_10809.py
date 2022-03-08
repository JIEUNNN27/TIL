#알파벳 찾기
word = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in word:
        index = word.find(i)
        print(index)
    else:
        print('-1')