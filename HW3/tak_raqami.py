n = int(input())
while n >= 10:
    summation = 0
    while n > 0:
        summation += (n % 10)
        n //= 10

    n = summation

print(n)
