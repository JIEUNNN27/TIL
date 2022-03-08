#크로아티아 알파벳
Word=input()


w1 = Word.replace('c=', '@')
w2 = w1.replace('c-', '@')
w3 = w2.replace('dz=','@')
w4 = w3.replace('d-', '@')
w5 = w4.replace('lj', '@')
w6 = w5.replace('nj', '@')
w7 = w6.replace('s=', '@')
w8 = w7.replace('z=', '@')

print(len(w8))
