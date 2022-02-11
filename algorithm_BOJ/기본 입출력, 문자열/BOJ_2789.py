email = input()
ban=list('CAMBRIDGE')

for a in ban:
    email = email.replace(a, '')
print(email)
