x = input().split()
r, c = int(x[0]), int(x[1])
if c <= 10:
    print("Right", 11 - r, c)
else:
    print("Left", 11 - r, 21 - c)
