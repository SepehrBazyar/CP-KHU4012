n, laptops = int(input()), []
for _ in range(n):
    laptops.append(tuple(map(int, input().split())))

flag = False
for laptop in laptops:
    for other_laptop in laptops:
        if (laptop[0] - other_laptop[0]) * (laptop[1] - other_laptop[1]) < 0:
            flag = True

print("happy aria" if flag else "poor aria")
