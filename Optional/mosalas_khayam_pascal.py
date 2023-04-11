n = int(input())
pre_line, current_line = [], []
for i in range(1, n + 1):
    for j in range(i):
        if j == 0 or j == i - 1:
            current_line.append(1)
        else:
            current_line.append(pre_line[j - 1] + pre_line[j])

    print(*current_line)
    pre_line, current_line = current_line, []
