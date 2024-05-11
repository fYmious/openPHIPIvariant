from itertools import product

num = 1 
for x in product("APRSU", repeat=5):
    word = "".join(x)
    if word.count("U") <= 1 and "AA" not in word:
        print(num, word)

    num += 1
