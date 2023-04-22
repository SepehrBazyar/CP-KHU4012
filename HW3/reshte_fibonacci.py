n = int(input())
signs = ["-"] * n
a, b = 1, 2
while b <= n:
    signs[a - 1] = signs[b - 1] = "+"
    a, b = b, a + b

print(*signs, sep="")
