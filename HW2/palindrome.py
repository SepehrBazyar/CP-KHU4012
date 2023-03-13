word = input().replace(' ', '').lower()
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")
