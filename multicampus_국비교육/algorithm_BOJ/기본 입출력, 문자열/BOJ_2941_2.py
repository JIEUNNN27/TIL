#크로아티아 알파벳
word = input()
calphabat = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for w in calphabat:
    if w in word:
        word = word.replace(w, '@')
    

print(len(word))