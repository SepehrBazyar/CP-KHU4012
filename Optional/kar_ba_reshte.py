word, result, VOWELS = input(), "", ("a", "e", "i", "o", "u")
for char in word:
    if char.lower() in VOWELS:
        result += "."
    elif char != " ":
        result += char.swapcase()

print(result)
