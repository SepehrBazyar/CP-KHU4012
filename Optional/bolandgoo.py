word = input()
for index, char in enumerate(word):
    print(char * (index + 1) + word[index + 1:])
