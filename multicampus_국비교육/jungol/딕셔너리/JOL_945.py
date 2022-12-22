#기타 자료형 - 자가진단5
animation = {
    "Pokemon":"Pikachu",
    "Digimon":"Agumon",
    "Yugioh" : "Black Magician"
}

word = input()

#세 개 중에 나오면 value/i don't know
# if word in animation:
#     print(animation[word])
# else:
#     print("I don't know")

#get을 쓰면 이렇게 된다. get(word,"None") 
print(animation.get(word,"I don't know"))