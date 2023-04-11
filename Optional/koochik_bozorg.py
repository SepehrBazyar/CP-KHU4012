word, lower, upper = input(), 0, 0
for char in word:
    if char.islower():
        lower += 1
    else:
        upper += 1

print(word.upper() if upper > lower else word.lower())
