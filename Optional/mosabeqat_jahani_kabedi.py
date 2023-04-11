n = int(input())
numbers, counter = map(int, input().split()), 0
for number in numbers:
    if number <= 2:
        counter += 1

print(counter // 3)
