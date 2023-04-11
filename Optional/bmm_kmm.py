n, m = map(int, input().split())
maximum, minimum = max(n, m), min(n, m)
while maximum % minimum != 0:
    maximum, minimum = minimum, maximum % minimum

print(minimum, n * m // minimum)
