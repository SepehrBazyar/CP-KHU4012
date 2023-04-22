n = int(input())
for i in range(1, n + 1):
    row = [i * j for j in range(1, n + 1)]
    print(*row)
