x = input().split()
angles = [int(x[0]), int(x[1]), int(x[2])]
print("Yes" if sum(angles) == 180 and 0 not in angles else "No")
