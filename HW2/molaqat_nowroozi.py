x = input().split()
places = [float(x[0]), float(x[1]), float(x[2])]
distance = max(places) - min(places)
print(int(distance) if distance.is_integer() else distance)
