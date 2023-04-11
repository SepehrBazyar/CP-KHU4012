number, summation = int(input()), 1
for i in range(2, number):
    if number % i == 0:
        summation += i

print("YES" if number == summation else "NO")
