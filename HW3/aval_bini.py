a = int(input())
b = int(input())
primes = []
for i in range(a + 1, b):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i > 1:
            primes.append(i)

print(*primes, sep=",")
